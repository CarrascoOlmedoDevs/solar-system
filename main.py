import pygame
# Asegúrate de tener un archivo celestial_body.py con la clase CuerpoCeleste
from celestial_body import CuerpoCeleste

# Inicializar Pygame
pygame.init()

# Definir constantes de pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Definir colores
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Crear la superficie de visualización (ventana)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Establecer el título de la ventana
pygame.display.set_caption("Sistema Solar Simple")

# Crear una instancia del Sol
# Posición central, radio grande, color amarillo
sun_pos = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
sun_radius = 50
sun_color = YELLOW
sun = CuerpoCeleste(sun_pos, sun_radius, sun_color)


# Bucle principal del juego
running = True
while running:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Lógica de actualización del juego ---
    # Aquí iría el código para actualizar el estado de los objetos del juego (posiciones, etc.)
    pass

    # --- Lógica de dibujo ---
    # Rellenar el fondo (ej. de negro)
    screen.fill(BLACK)

    # Dibujar el Sol
    sun.draw(screen)

    # Dibujar otros objetos (planetas, etc.) aquí

    # Actualizar la pantalla
    pygame.display.flip() # O pygame.display.update()

# Salir de Pygame
pygame.quit()
# sys.exit() # Opcional: para salir completamente del script