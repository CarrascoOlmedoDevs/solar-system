# main.py
import pygame
import sys
from celestial_body import CelestialBody

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulación Gravitatoria")

# Crear cuerpos celestes (placeholder)
# body1 = CelestialBody(mass=1000, radius=20, pos_x=WIDTH // 4, pos_y=HEIGHT // 2, vel_x=0, vel_y=0, color=(255, 255, 0))
# body2 = CelestialBody(mass=500, radius=10, pos_x=3 * WIDTH // 4, pos_y=HEIGHT // 2, vel_x=0, vel_y=5, color=(0, 0, 255))
# celestial_bodies = [body1, body2]
celestial_bodies = [] # Lista vacía por ahora

# Bucle principal del juego
running = True
while running:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar (placeholder)
    # Aquí iría la lógica de actualización de posiciones/velocidades
    pass

    # Dibujar
    screen.fill((0, 0, 0)) # Fondo negro

    # Dibujar cuerpos celestes (placeholder)
    for body in celestial_bodies:
        body.draw(screen)

    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
sys.exit()
```
```python
# celestial_body.py
import pygame

class CelestialBody:
    def __init__(self, mass, radius, pos_x, pos_y, vel_x, vel_y, color):
        self.mass = mass
        self.radius = radius
        self.position = pygame.math.Vector2(pos_x, pos_y)
        self.velocity = pygame.math.Vector2(vel_x, vel_y)
        self.color = color

    def draw(self, screen):
        # Placeholder para dibujar el cuerpo celeste
        # Implementación futura: dibujar un círculo
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.radius)

    # Métodos futuros para calcular fuerzas, actualizar posición, etc.
    # def apply_force(self, force): pass
    # def update(self, dt): pass