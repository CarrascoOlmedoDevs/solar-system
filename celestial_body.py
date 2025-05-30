import pygame
import math

class CuerpoCeleste:
    """Representa un cuerpo celeste (estrella, planeta, luna, etc.) en una simulación."""

    def __init__(self, x, y, radius, color, mass,
                 parent=None,
                 orbital_radius=0, # Distancia desde el centro del padre
                 orbital_angle=0,  # Ángulo inicial en radianes alrededor del padre
                 orbital_speed=0,  # Velocidad angular en radianes por actualización (anulada por orbital_period si se proporciona)
                 orbital_period_around_parent=None, # Unidades de tiempo para una órbita completa alrededor del padre
                 ring_radius_inner=None,
                 ring_radius_outer=None,
                 ring_color=None):

        # Atributos principales
        # Posición absoluta para el cuerpo principal (si no tiene padre), o posición inicial (si tiene padre)
        self.x = x
        # Posición absoluta para el cuerpo principal (si no tiene padre), o posición inicial (si tiene padre)
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        # Atributos orbitales (si este cuerpo orbita a un padre)
        self.parent = parent # Referencia al cuerpo padre
        self.orbital_radius = orbital_radius # Distancia desde el padre
        # Ángulo actual en radianes alrededor del padre (se actualiza con el tiempo)
        self.orbital_angle = orbital_angle

        # Calcular la velocidad orbital a partir del período si se proporciona, de lo contrario usar orbital_speed
        self.orbital_speed = orbital_speed # Velocidad por defecto o proporcionada
        if orbital_period_around_parent is not None and orbital_period_around_parent != 0:
            # Calcular velocidad a partir del período: 2*pi radianes / período
            self.orbital_speed = (2 * math.pi) / orbital_period_around_parent

        # Atributos de anillos (si este cuerpo tiene anillos)
        self.ring_radius_inner = ring_radius_inner
        self.ring_radius_outer = ring_radius_outer
        self.ring_color = ring_color
        # Determinar si el cuerpo tiene anillos basándose en radios válidos proporcionados
        self.has_rings = (ring_radius_inner is not None and ring_radius_outer is not None and
                          0 <= ring_radius_inner < ring_radius_outer) # Asegurar radios válidos: interior >= 0, interior < exterior

        # Lista para almacenar cuerpos que orbitan a este cuerpo (lunas, etc.)
        self.moons = []

        # Si este cuerpo tiene un padre, calcular su posición inicial basándose en el padre
        # Esto asegura que la posición inicial x, y sea correcta inmediatamente después de la creación
        if self.parent is not None:
             parent_x = self.parent.x
             parent_y = self.parent.y
             self.x = parent_x + self.orbital_radius * math.cos(self.orbital_angle)
             self.y = parent_y + self.orbital_radius * math.sin(self.orbital_angle)


    def add_moon(self, moon):
        """Añade un cuerpo (luna, etc.) a la lista de cuerpos que orbitan a este cuerpo."""
        # Asegurar que el padre del cuerpo añadido sea este cuerpo
        moon.parent = self
        # El cuerpo añadido debería haber sido inicializado con sus parámetros orbitales
        # relativos a su padre previsto (este cuerpo).
        self.moons.append(moon)

    def update(self):
        """
        Actualiza la posición del cuerpo celeste y de los cuerpos que lo orbitan (lunas).
        Si el cuerpo tiene un padre, su posición se calcula en relación con el padre.
        De lo contrario, su posición se asume como absoluta (ej. una estrella en el centro).
        """
        if self.parent is not None:
            # Este cuerpo está orbitando a un padre
            # Calcular la posición absoluta basándose en el padre y los parámetros orbitales
            parent_x = self.parent.x
            parent_y = self.parent.y

            self.x = parent_x + self.orbital_radius * math.cos(self.orbital_angle)
            self.y = parent_y + self.orbital_radius * math.sin(self.orbital_angle)

            # Actualizar el ángulo orbital para el siguiente paso
            self.orbital_angle += self.orbital_speed
            # Envolver el ángulo para mantenerlo dentro de [0, 2*pi) por estabilidad numérica
            self.orbital_angle %= (2 * math.pi)

        # Actualizar las posiciones de cualquier cuerpo que orbite a este cuerpo (lunas)
        for moon in self.moons:
            moon.update()

    def draw(self, surface, bg_color):
        """
        Dibuja el cuerpo celeste, sus anillos y los cuerpos que lo orbitan (lunas)
        en la superficie dada.

        Args:
            surface: La superficie de pygame sobre la que dibujar.
            bg_color: El color de fondo, usado para dibujar los anillos.
        """
        # Dibujar los anillos primero, si existen, para asegurar que estén detrás del cuerpo
        if self.has_rings:
            # Dibujar el anillo exterior (círculo relleno)
            # Asegurar que el radio sea positivo antes de dibujar
            if self.ring_radius_outer is not None and self.ring_radius_outer > 0:
                 pygame.draw.circle(surface, self.ring_color, (int(self.x), int(self.y)), int(self.ring_radius_outer))
            # Dibujar la parte interior con el color de fondo para crear el efecto de anillo
            # Asegurar que el radio sea no negativo antes de dibujar
            if self.ring_radius_inner is not None and self.ring_radius_inner >= 0:
                 pygame.draw.circle(surface, bg_color, (int(self.x), int(self.y)), int(self.ring_radius_inner))


        # Dibujar el cuerpo principal (círculo relleno) encima de los anillos
        # Asegurar que el radio sea positivo antes de dibujar
        if self.radius > 0:
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), int(self.radius))

        # Dibujar cualquier cuerpo que orbite a este cuerpo (lunas)
        for moon in self.moons:
            moon.draw(surface, bg_color) # Dibujar lunas recursivamente