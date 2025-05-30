import pygame
import math

class CuerpoCeleste:
    def __init__(self, x, y, radius, color, mass,
                 parent=None,
                 orbital_radius=0, # Distance from parent
                 orbital_angle=0,  # Initial angle in radians around parent
                 orbital_speed=0,  # Speed in radians per update (overridden by orbital_period if provided)
                 orbital_period_around_parent=None, # Time units for one orbit
                 ring_radius_inner=None,
                 ring_radius_outer=None,
                 ring_color=None):

        # Core attributes
        self.x = x # Absolute position for the main body, or calculated position for a moon
        self.y = y # Absolute position for the main body, or calculated position for a moon
        self.radius = radius
        self.color = color
        self.mass = mass

        # Orbital attributes (if this body orbits a parent)
        self.parent = parent # Reference to the parent body
        self.orbital_radius = orbital_radius # Distance from parent
        self.orbital_angle = orbital_angle # Current angle in radians around parent

        # Calculate orbital speed
        self.orbital_speed = orbital_speed # Default or provided speed
        if orbital_period_around_parent is not None and orbital_period_around_parent != 0:
            # Calculate speed from period: 2*pi radians / period
            self.orbital_speed = (2 * math.pi) / orbital_period_around_parent

        # Ring attributes (if this body has rings)
        self.ring_radius_inner = ring_radius_inner
        self.ring_radius_outer = ring_radius_outer
        self.ring_color = ring_color
        # Determine if the body has rings based on provided radii
        self.has_rings = (ring_radius_inner is not None and ring_radius_outer is not None and
                          ring_radius_inner < ring_radius_outer) # Ensure valid radii

        # List to hold moons orbiting this body
        self.moons = []

    def add_moon(self, moon):
        """Adds a moon to this body's list of moons."""
        self.moons.append(moon)
        moon.parent = self # Set the parent reference on the moon

    def update(self):
        """
        Updates the position of the celestial body and its moons.
        If the body has a parent, its position is calculated relative to the parent.
        Otherwise, its position is assumed to be absolute or handled externally.
        """
        if self.parent is not None:
            # This body is a moon orbiting a parent
            # Calculate absolute position based on parent and orbital parameters
            parent_x = self.parent.x
            parent_y = self.parent.y

            self.x = parent_x + self.orbital_radius * math.cos(self.orbital_angle)
            self.y = parent_y + self.orbital_radius * math.sin(self.orbital_angle)

            # Update orbital angle for the next step
            self.orbital_angle += self.orbital_speed
            # Keep angle within [0, 2*pi)
            # This prevents floating point issues with large angles over time
            self.orbital_angle %= (2 * math.pi)
            # Ensure positive angle if it wrapped below zero (though modulo handles positive speeds)
            if self.orbital_angle < 0:
                 self.orbital_angle += (2 * math.pi)


        # Update moons orbiting this body
        # Pass this body's current position as the parent position for the moon update
        for moon in self.moons:
            moon.update() # Moons will use their own self.parent reference

    def draw_rings(self, surface, offset_x=0, offset_y=0):
        """Dibuja los anillos alrededor del cuerpo celeste."""
        if self.has_rings:
            center_x = int(self.x + offset_x)
            center_y = int(self.y + offset_y)

            # Draw rings as concentric circles
            # A simple way is to draw the outer ring and then the inner ring in background color
            # A better way for transparency/texture would be more complex, but this works for solid rings
            # Draw outer ring
            outer_rect = pygame.Rect(0, 0, self.ring_radius_outer * 2, self.ring_radius_outer * 2)
            outer_rect.center = (center_x, center_y)
            pygame.draw.ellipse(surface, self.ring_color, outer_rect, width=int(self.ring_radius_outer - self.ring_radius_inner))

            # Alternatively, draw multiple thin ellipses for a banded look (optional)
            # num_bands = 10
            # band_width = (self.ring_radius_outer - self.ring_radius_inner) / num_bands
            # for i in range(num_bands):
            #     r = self.ring_radius_inner + i * band_width + band_width / 2
            #     ring_rect = pygame.Rect(0, 0, r * 2, r * 2)
            #     ring_rect.center = (center_x, center_y)
            #     pygame.draw.ellipse(surface, self.ring_color, ring_rect, width=int(band_width))


    def draw(self, surface, offset_x=0, offset_y=0):
        """
        Dibuja el cuerpo celeste, sus anillos (si los tiene) y sus lunas.
        offset_x, offset_y se usan para desplazar la vista (cámara).
        """
        # Draw rings first so they are behind the body
        if self.has_rings:
            self.draw_rings(surface, offset_x, offset_y)

        # Draw the body itself
        center_x = int(self.x + offset_x)
        center_y = int(self.y + offset_y)
        pygame.draw.circle(surface, self.color, (center_x, center_y), int(self.radius))

        # Draw moons orbiting this body
        for moon in self.moons:
            moon.draw(surface, offset_x, offset_y)