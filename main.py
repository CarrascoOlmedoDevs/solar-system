import pygame
import sys # Importar sys para sys.exit() opcional
# Asegúrate de tener un archivo celestial_body.py con la clase CuerpoCeleste
from celestial_body import CuerpoCeleste
import math # Necesario si se implementa física real, pero útil para cálculos de posición/velocidad inicial

# Inicializar Pygame
pygame.init()

# Definir constantes de pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Definir colores
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREY = (150, 150, 150)
ORANGE = (255, 165, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Crear la superficie de visualización (ventana)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Establecer el título de la ventana
pygame.display.set_caption("Sistema Solar Simple")

# Crear una lista para almacenar todos los cuerpos celestes
cuerpos_celestes = []

# Definir la posición central del Sol
sun_center_x = SCREEN_WIDTH // 2
sun_center_y = SCREEN_HEIGHT // 2

# Crear una instancia del Sol
# Nombre, masa (placeholder grande), radio, color, posición (vector), velocidad (vector)
# Usamos listas mutables para posición y velocidad
sun_pos = [sun_center_x, sun_center_y]
sun_vel = [0, 0]
# Reducimos el radio del Sol para dejar espacio a los planetas
sun = CuerpoCeleste("Sol", 1.989e30, 20, YELLOW, sun_pos, sun_vel)
cuerpos_celestes.append(sun)

# Crear instancias de los planetas interiores
# Definir distancias orbitales relativas (en píxeles)
distancia_mercurio = 50
distancia_venus = 80
distancia_tierra = 120
distancia_marte = 180

# Las velocidades iniciales se establecen tangenciales a la órbita inicial
# y con magnitudes placeholder. La física real se añadiría en la lógica de actualización.

# Mercurio
mercury_pos = [sun_center_x + distancia_mercurio, sun_center_y]
mercury_vel = [0, -5] # Placeholder: velocidad hacia arriba (tangencial si empieza a la derecha)
mercury = CuerpoCeleste("Mercurio", 0.330e24, 3, GREY, mercury_pos, mercury_vel)
cuerpos_celestes.append(mercury)

# Venus
venus_pos = [sun_center_x + distancia_venus, sun_center_y]
venus_vel = [0, -4] # Placeholder
venus = CuerpoCeleste("Venus", 4.867e24, 6, ORANGE, venus_pos, venus_vel)
cuerpos_celestes.append(venus)

# Tierra
earth_pos = [sun_center_x + distancia_tierra, sun_center_y]
earth_vel = [0, -3.5] # Placeholder
earth = CuerpoCeleste("Tierra", 5.972e24, 8, BLUE, earth_pos, earth_vel)
cuerpos_celestes.append(earth)

# Marte
mars_pos = [sun_center_x + distancia_marte, sun_center_y]
mars_vel = [0, -3] # Placeholder
mars = CuerpoCeleste("Marte", 0.642e24, 5, RED, mars_pos, mars_vel)
cuerpos_celestes.append(mars)


# Bucle principal del juego
running = True
while running:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Lógica de actualización del juego ---
    # Aquí iría el código para actualizar el estado de los objetos del juego (posiciones, etc.)
    # Por ahora, simplemente pasamos, como en el código original.
    # En una versión completa, se calcularían las fuerzas gravitatorias y se actualizarían
    # las velocidades y posiciones de cada cuerpo (excepto el Sol si es fijo).
    pass

    # --- Lógica de dibujo ---
    # Rellenar el fondo (ej. de negro)
    screen.fill(BLACK)

    # Dibujar todos los cuerpos celestes en la lista
    for body in cuerpos_celestes:
        body.draw(screen)

    # Actualizar la pantalla
    pygame.display.flip() # O pygame.display.update()

# Salir de Pygame
pygame.quit()
# sys.exit() # Opcional: para salir completamente del script