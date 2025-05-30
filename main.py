import pygame
import sys
# Asegúrate de tener un archivo celestial_body.py con la clase CuerpoCeleste
# Asumimos que CuerpoCeleste ahora acepta un argumento 'parent' y 'has_rings'
from celestial_body import CuerpoCeleste
import math # math might be needed for vector calculations or physics

# Inicializar Pygame
pygame.init()

# Definir constantes de pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255) # Color para las órbitas (si se dibujaran)
YELLOW = (255, 255, 0) # Sol
GREY = (150, 150, 150) # Mercurio, Luna
ORANGE = (255, 165, 0) # Venus, Titan
BLUE = (0, 0, 255) # Tierra
RED = (255, 0, 0) # Marte, Phobos, Deimos (rojizos)
BROWN = (139, 69, 19) # Jupiter
LIGHT_GREY = (200, 200, 200) # Saturno
LIGHT_BLUE = (173, 216, 230) # Urano
DARK_BLUE = (0, 0, 139) # Neptuno
LIGHT_ORANGE = (255, 200, 0) # Io
LIGHT_BROWN = (180, 120, 60) # Europa
DARK_GREY = (100, 100, 100) # Ganymede
DARK_BROWN = (80, 50, 20) # Callisto


# Crear la superficie de visualización (ventana)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Establecer el título de la ventana
pygame.display.set_caption("Sistema Solar Simple con Gravedad N-body (Escalado y Centrado)")

# Crear una lista para almacenar todos los cuerpos celestes
cuerpos_celestes = []

# Definir la posición central del Sol en el sistema de coordenadas "real" (no escalado)
# Este punto será el origen (0,0) después de aplicar la traslación antes del escalado
# Para simplificar, usamos directamente las coordenadas de pantalla para la posición inicial del Sol
sun_center_x = SCREEN_WIDTH // 2
sun_center_y = SCREEN_HEIGHT // 2

# Crear una instancia del Sol
# Nombre, masa (placeholder grande), radio, color, posición (vector), velocidad (vector), radio_orbital (0 para el sol), parent (None), has_rings (False)
# Usamos listas mutables para posición y velocidad
sun_pos = [float(sun_center_x), float(sun_center_y)] # Usar float para mayor precisión
sun_vel = [0.0, 0.0] # El sol no se mueve en este modelo simplificado (centro del sistema)
# Reducimos el radio del Sol para dejar espacio a los planetas
# La masa del sol es mucho mayor que la de los planetas
sun = CuerpoCeleste("Sol", 1.989e30, 20, YELLOW, sun_pos, sun_vel, 0, None, False) # El sol no tiene órbita alrededor de sí mismo
cuerpos_celestes.append(sun)

# Crear instancias de los planetas
# Definir distancias orbitales relativas (en píxeles) desde el centro del Sol
# Estas son distancias iniciales. La simulación N-body ajustará las posiciones.
# Usamos distancias relativas para que el sistema quepa inicialmente,
# aunque la simulación real usaría unidades astronómicas escaladas.
distancia_mercurio = 50
distancia_venus = 80
distancia_tierra = 120
distancia_marte = 180
distancia_jupiter = 300 # Distancias aumentadas para incluir planetas exteriores
distancia_saturno = 400
distancia_urano = 500
distancia_neptuno = 600 # Este será el radio máximo para el escalado

# Las velocidades iniciales se establecen tangenciales a la órbita inicial
# y con magnitudes placeholder. La física real se añadiría en la lógica de actualización.
# Para órbitas circulares estables alrededor del Sol, la velocidad inicial v
# sería proporcional a sqrt(M_sol / r). Usaremos valores relativos simples.

# Posición inicial: (distancia, 0) relativa al Sol (en el lado derecho)
# Velocidad inicial: (0, -velocidad_tangencial) para órbita CCW

# Mercurio
mercurio_pos = [float(sun_center_x + distancia_mercurio), float(sun_center_y)]
mercurio_vel = [0.0, -3.0] # Placeholder velocity (pixels/frame)
mercurio = CuerpoCeleste("Mercurio", 3.301e23, 5, GREY, mercurio_pos, mercurio_vel, distancia_mercurio, sun, False)
cuerpos_celestes.append(mercurio)

# Venus
venus_pos = [float(sun_center_x + distancia_venus), float(sun_center_y)]
venus_vel = [0.0, -2.5] # Placeholder velocity
venus = CuerpoCeleste("Venus", 4.867e24, 8, ORANGE, venus_pos, venus_vel, distancia_venus, sun, False)
cuerpos_celestes.append(venus)

# Tierra
tierra_pos = [float(sun_center_x + distancia_tierra), float(sun_center_y)]
tierra_vel = [0.0, -2.0] # Placeholder velocity
tierra = CuerpoCeleste("Tierra", 5.972e24, 10, BLUE, tierra_pos, tierra_vel, distancia_tierra, sun, False)
cuerpos_celestes.append(tierra)

# Marte
marte_pos = [float(sun_center_x + distancia_marte), float(sun_center_y)]
marte_vel = [0.0, -1.5] # Placeholder velocity
marte = CuerpoCeleste("Marte", 6.417e23, 7, RED, marte_pos, marte_vel, distancia_marte, sun, False)
cuerpos_celestes.append(marte)

# Jupiter
jupiter_pos = [float(sun_center_x + distancia_jupiter), float(sun_center_y)]
jupiter_vel = [0.0, -1.0] # Placeholder velocity
jupiter = CuerpoCeleste("Jupiter", 1.898e27, 15, BROWN, jupiter_pos, jupiter_vel, distancia_jupiter, sun, False)
cuerpos_celestes.append(jupiter)

# Saturno
saturno_pos = [float(sun_center_x + distancia_saturno), float(sun_center_y)]
saturno_vel = [0.0, -0.8] # Placeholder velocity
saturno = CuerpoCeleste("Saturno", 5.683e26, 13, LIGHT_GREY, saturno_pos, saturno_vel, distancia_saturno, sun, True) # Saturno tiene anillos
cuerpos_celestes.append(saturno)

# Urano
urano_pos = [float(sun_center_x + distancia_urano), float(sun_center_y)]
urano_vel = [0.0, -0.6] # Placeholder velocity
urano = CuerpoCeleste("Urano", 8.681e25, 12, LIGHT_BLUE, urano_pos, urano_vel, distancia_urano, sun, False)
cuerpos_celestes.append(urano)

# Neptuno
neptuno_pos = [float(sun_center_x + distancia_neptuno), float(sun_center_y)]
neptuno_vel = [0.0, -0.5] # Placeholder velocity
neptuno = CuerpoCeleste("Neptuno", 1.024e26, 12, DARK_BLUE, neptuno_pos, neptuno_vel, distancia_neptuno, sun, False)
cuerpos_celestes.append(neptuno)

# --- Bucle Principal del Juego ---
running = True
clock = pygame.time.Clock() # Para controlar el framerate

while running:
    # --- Manejo de Eventos ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Aquí se podrían añadir otros manejadores de eventos (ej. teclado, ratón)

    # --- Lógica de Actualización ---
    # Aquí iría la lógica de la simulación N-body (cálculo de fuerzas, actualización de velocidad y posición)
    # Se necesitaría un timestep (dt) para una simulación física correcta
    # dt = clock.tick(60) / 1000.0 # Delta time in seconds (if implementing physics)

    # Por ahora, solo llamamos a un método de actualización si existe,
    # que podría simplemente mover el cuerpo basándose en su velocidad actual.
    # La lógica N-body real implicaría calcular fuerzas *antes* de actualizar velocidades y posiciones.
    for body in cuerpos_celestes:
        # Asumimos que CuerpoCeleste tiene un método update() que aplica la velocidad a la posición
        # Si se implementa N-body, este update sería llamado *después* de calcular las nuevas velocidades
        # body.update() # Descomentar si CuerpoCeleste.update() maneja el movimiento simple vel -> pos
        pass # Placeholder for the actual physics update logic

    # --- Lógica de Dibujo ---
    # Rellenar el fondo
    screen.fill(BLACK)

    # Dibujar cada cuerpo celeste
    for body in cuerpos_celestes:
        # Asumimos que la clase CuerpoCeleste tiene un método draw(surface)
        body.draw(screen)

    # --- Actualizar Pantalla ---
    pygame.display.flip() # O pygame.display.update()

    # --- Control de Framerate ---
    clock.tick(60) # Limitar a 60 FPS

# --- Salir de Pygame ---
pygame.quit()
sys.exit()