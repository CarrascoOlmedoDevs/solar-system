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
WHITE = (255, 255, 255) # Color para las órbitas
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
# Nombre, masa (placeholder grande), radio, color, posición (vector), velocidad (vector), radio_orbital (0 para el sol)
# Usamos listas mutables para posición y velocidad
sun_pos = [float(sun_center_x), float(sun_center_y)] # Usar float para mayor precisión si se implementa física
sun_vel = [0.0, 0.0]
# Reducimos el radio del Sol para dejar espacio a los planetas
sun = CuerpoCeleste("Sol", 1.989e30, 20, YELLOW, sun_pos, sun_vel, 0) # El sol no tiene órbita alrededor de sí mismo
cuerpos_celestes.append(sun)

# Crear instancias de los planetas interiores
# Definir distancias orbitales relativas (en píxeles)
distancia_mercurio = 50
distancia_venus = 80
distancia_tierra = 120
distancia_marte = 180

# Las velocidades iniciales se establecen tangenciales a la órbita inicial
# y con magnitudes placeholder. La física real se añadiría en la lógica de actualización.
# Posición inicial: [sun_center_x + distancia, sun_center_y] (a la derecha del sol)
# Velocidad inicial placeholder: [0, -velocidad_placeholder] (hacia arriba para órbita anti-horaria simple)

# Mercurio
mercury_orbital_radius = distancia_mercurio
mercury_pos = [float(sun_center_x + mercury_orbital_radius), float(sun_center_y)]
mercury_vel = [0.0, -5.0] # Placeholder: velocidad hacia arriba
mercury = CuerpoCeleste("Mercurio", 0.330e24, 3, GREY, mercury_pos, mercury_vel, mercury_orbital_radius)
cuerpos_celestes.append(mercury)

# Venus
venus_orbital_radius = distancia_venus
venus_pos = [float(sun_center_x + venus_orbital_radius), float(sun_center_y)]
venus_vel = [0.0, -4.0] # Placeholder
venus = CuerpoCeleste("Venus", 4.867e24, 6, ORANGE, venus_pos, venus_vel, venus_orbital_radius)
cuerpos_celestes.append(venus)

# Tierra
earth_orbital_radius = distancia_tierra
earth_pos = [float(sun_center_x + earth_orbital_radius), float(sun_center_y)]
earth_vel = [0.0, -3.5] # Placeholder
earth = CuerpoCeleste("Tierra", 5.972e24, 8, BLUE, earth_pos, earth_vel, earth_orbital_radius)
cuerpos_celestes.append(earth)

# Marte
mars_orbital_radius = distancia_marte
mars_pos = [float(sun_center_x + mars_orbital_radius), float(sun_center_y)]
mars_vel = [0.0, -3.0] # Placeholder
mars = CuerpoCeleste("Marte", 0.642e24, 5, RED, mars_pos, mars_vel, mars_orbital_radius)
cuerpos_celestes.append(mars)


# Bucle principal del juego
running = True
# Podemos usar un reloj para controlar la velocidad de la simulación si es necesario
# clock = pygame.time.Clock()

while running:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Lógica de actualización del juego ---
    # Aquí iría el código para actualizar el estado de los objetos del juego (posiciones, etc.)
    # Si se implementa física real, se calcularían las fuerzas gravitatorias y se actualizarían
    # las velocidades y posiciones.
    # delta_time = clock.tick(60) / 1000.0 # Tiempo en segundos desde el último frame (si usas clock)

    # Ejemplo de actualización simple (mover con velocidad constante)
    # for body in cuerpos_celestes:
    #    body.actualizar(1) # Pasar un delta_time fijo o real

    # --- Lógica de dibujo ---
    # Limpiar la pantalla
    screen.fill(BLACK)

    # Dibujar las órbitas (círculos centrados en el Sol)
    # Asumimos que el Sol es el primer cuerpo en la lista para obtener su posición central
    sun_pos_actual = cuerpos_celestes[0].posicion
    for body in cuerpos_celestes:
        # Dibujar órbita solo si no es el sol y tiene un radio orbital definido
        if body.nombre != "Sol" and body.orbital_radius > 0:
            # Dibujar un círculo con centro en la posición del sol y radio orbital del planeta
            pygame.draw.circle(screen, WHITE, (int(sun_pos_actual[0]), int(sun_pos_actual[1])), body.orbital_radius, 1) # El último parámetro es el grosor de la línea

    # Dibujar cada cuerpo celeste
    for body in cuerpos_celestes:
        body.dibujar(screen) # Asumimos que la clase CuerpoCeleste tiene un método dibujar

    # Actualizar la pantalla para mostrar los cambios
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
sys.exit()