import pygame

class CuerpoCeleste:
    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

    def draw(self, surface):
        """Dibuja el cuerpo celeste en la superficie de Pygame."""
        # Pygame circle function expects integer coordinates and radius
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), int(self.radius))

    # Optional: Add methods for physics calculations later (e.g., update_position, apply_force)
    # For this task, only __init__ and draw are required.

if __name__ == '__main__':
    # Example usage (optional, for testing the class)
    pygame.init()
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Cuerpo Celeste Test")

    # Define colors
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)
    BLUE = (0, 0, 255)

    # Create a celestial body instance (e.g., a small blue planet)
    planet = CuerpoCeleste(x=screen_width // 2, y=screen_height // 2, radius=20, color=BLUE, mass=1000)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill((0, 0, 0)) # Black background

        # Draw the celestial body
        planet.draw(screen)

        # Update the display
        pygame.display.flip()

    pygame.quit()