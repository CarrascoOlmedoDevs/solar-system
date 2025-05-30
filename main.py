import pygame
import sys
# Asegúrate de tener un archivo celestial_body.py con la clase CuerpoCeleste
from celestial_body import CuerpoCeleste
import math

# Inicializar Pygame
pygame.init()

# Definir constantes de pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255) # Color para las órbitas (si se dibujaran)
YELLOW = (255, 255, 0) # Sol
GREY = (150, 150, 150) # Mercurio
ORANGE = (255, 165, 0) # Venus
BLUE = (0, 0, 255) # Tierra
RED = (255, 0, 0) # Marte
BROWN = (139, 69, 19) # Jupiter
LIGHT_GREY = (200, 200, 200) # Saturno
LIGHT_BLUE = (173, 216, 230) # Urano
DARK_BLUE = (0, 0, 139) # Neptuno


# Crear la superficie de visualización (ventana)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Establecer el título de la ventana
pygame.display.set_caption("Sistema Solar Simple con Gravedad N-body (Escalado y Centrado)")

# Crear una lista para almacenar todos los cuerpos celestes
cuerpos_celestes = []

# Definir la posición central del Sol en el sistema de coordenadas "real" (no escalado)
# Este punto será el origen (0,0) después de aplicar la traslación antes del escalado
sun_center_x = SCREEN_WIDTH // 2
sun_center_y = SCREEN_HEIGHT // 2

# Crear una instancia del Sol
# Nombre, masa (placeholder grande), radio, color, posición (vector), velocidad (vector), radio_orbital (0 para el sol)
# Usamos listas mutables para posición y velocidad
sun_pos = [float(sun_center_x), float(sun_center_y)] # Usar float para mayor precisión si se implementa física
sun_vel = [0.0, 0.0]
# Reducimos el radio del Sol para dejar espacio a los planetas
# La masa del sol es mucho mayor que la de los planetas
sun = CuerpoCeleste("Sol", 1.989e30, 20, YELLOW, sun_pos, sun_vel, 0) # El sol no tiene órbita alrededor de sí mismo
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
# Para órbitas circulares estables, la velocidad inicial v = sqrt(G*M/r) donde M es la masa del cuerpo central (Sol)
# y r es la distancia orbital. Usaremos placeholders por ahora, pero la simulación N-body ajustará esto.
# Posición inicial: [sun_center_x + distancia, sun_center_y] (a la derecha del sol)
# Velocidad inicial placeholder: [0, -velocidad_placeholder] (hacia arriba para órbita anti-horaria simple)
# NOTA: Estas velocidades placeholder son ARBITRARIAS y probablemente no resultarán en órbitas estables sin una implementación
# correcta de la física N-body y una constante gravitacional escalada apropiadamente.

# Mercurio
mercury_orbital_radius = distancia_mercurio
mercury_pos = [float(sun_center_x + mercury_orbital_radius), float(sun_center_y)]
mercury_vel = [0.0, -5.0] # Placeholder velocity
mercury = CuerpoCeleste("Mercurio", 0.330e24, 3, GREY, mercury_pos, mercury_vel, mercury_orbital_radius)
cuerpos_celestes.append(mercury)

# Venus
venus_orbital_radius = distancia_venus
venus_pos = [float(sun_center_x + venus_orbital_radius), float(sun_center_y)]
venus_vel = [0.0, -4.0] # Placeholder velocity
venus = CuerpoCeleste("Venus", 4.867e24, 5, ORANGE, venus_pos, venus_vel, venus_orbital_radius)
cuerpos_celestes.append(venus)

# Tierra
earth_orbital_radius = distancia_tierra
earth_pos = [float(sun_center_x + earth_orbital_radius), float(sun_center_y)]
earth_vel = [0.0, -3.0] # Placeholder velocity
earth = CuerpoCeleste("Tierra", 5.972e24, 6, BLUE, earth_pos, earth_vel, earth_orbital_radius)
cuerpos_celestes.append(earth)

# Marte
mars_orbital_radius = distancia_marte
mars_pos = [float(sun_center_x + mars_orbital_radius), float(sun_center_y)]
mars_vel = [0.0, -2.5] # Placeholder velocity
mars = CuerpoCeleste("Marte", 0.642e24, 4, RED, mars_pos, mars_vel, mars_orbital_radius)
cuerpos_celestes.append(mars)

# Jupiter
jupiter_orbital_radius = distancia_jupiter
jupiter_pos = [float(sun_center_x + jupiter_orbital_radius), float(sun_center_y)]
jupiter_vel = [0.0, -1.5] # Placeholder velocity
jupiter = CuerpoCeleste("Jupiter", 1898e24, 15, BROWN, jupiter_pos, jupiter_vel, jupiter_orbital_radius)
cuerpos_celestes.append(jupiter)

# Saturno
saturn_orbital_radius = distancia_saturno
saturn_pos = [float(sun_center_x + saturn_orbital_radius), float(sun_center_y)]
saturn_vel = [0.0, -1.2] # Placeholder velocity
saturn = CuerpoCeleste("Saturno", 568e24, 12, LIGHT_GREY, saturn_pos, saturn_vel, saturn_orbital_radius)
cuerpos_celestes.append(saturn)

# Urano
uranus_orbital_radius = distancia_urano
uranus_pos = [float(sun_center_x + uranus_orbital_radius), float(sun_center_y)]
uranus_vel = [0.0, -1.0] # Placeholder velocity
uranus = CuerpoCeleste("Urano", 86.8e24, 8, LIGHT_BLUE, uranus_pos, uranus_vel, uranus_orbital_radius)
cuerpos_celestes.append(uranus)

# Neptuno
neptune_orbital_radius = distancia_neptuno
neptune_pos = [float(sun_center_x + neptune_orbital_radius), float(sun_center_y)]
neptune_vel = [0.0, -0.8] # Placeholder velocity
neptune = CuerpoCeleste("Neptuno", 102e24, 8, DARK_BLUE, neptune_pos, neptune_vel, neptune_orbital_radius)
cuerpos_celestes.append(neptune)


# --- Lógica de Escalado y Centrado ---

# Calcular el radio máximo necesario para visualizar todo el sistema
# Esto se basa en la distancia orbital del planeta más lejano desde el Sol.
# Si el Sol no está en (0,0) en el sistema de coordenadas "real",
# deberíamos considerar la distancia máxima de CUALQUIER cuerpo a CUALQUIER otro cuerpo,
# pero asumiendo que el Sol es el centro y los planetas orbitan a su alrededor,
# la distancia máxima es simplemente la del planeta más lejano al Sol.
# En nuestro caso, es la distancia_neptuno.
max_system_radius = distancia_neptuno

# Definir un margen para que el sistema no toque los bordes de la ventana
margin = 50 # Píxeles

# Calcular el factor de escala
# El sistema ocupa un área de (2 * max_system_radius) x (2 * max_system_radius)
# en el sistema de coordenadas "real" centrado en el Sol.
# Necesitamos que esto quepa dentro de (SCREEN_WIDTH - 2*margin) x (SCREEN_HEIGHT - 2*margin).
# El factor de escala es el mínimo de las proporciones de ancho y alto disponibles.
available_width = SCREEN_WIDTH - 2 * margin
available_height = SCREEN_HEIGHT - 2 * margin
required_size = 2 * max_system_radius

# Asegurarse de que required_size no sea cero para evitar división por cero
if required_size <= 0:
    scale_factor = 1.0 # No escalar si no hay cuerpos o distancias
else:
    scale_factor = min(available_width, available_height) / required_size

# Calcular el desplazamiento para centrar el sistema escalado
# El centro del sistema "real" (el Sol) debe ir al centro de la pantalla.
offset_x = SCREEN_WIDTH // 2
offset_y = SCREEN_HEIGHT // 2

# --- Bucle principal del juego ---
running = True
while running:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Lógica de actualización (placeholder) ---
    # Aquí iría la lógica para actualizar las posiciones y velocidades
    # de los cuerpos celestes basada en la física N-body.
    # Por ahora, solo se mantienen las posiciones iniciales o se aplican velocidades placeholder.
    # for body in cuerpos_celestes:
    #     body.update_position(1.0) # Ejemplo: actualizar posición basado en velocidad actual
    #     body.apply_gravity(cuerpos_celestes) # Ejemplo: calcular y aplicar fuerzas gravitatorias

    # Limpiar la pantalla
    screen.fill(BLACK)

    # --- Dibujar cuerpos celestes (aplicando escalado y centrado) ---
    for body in cuerpos_celestes:
        # Calcular la posición de dibujo aplicando traslación (centrar en el Sol original)
        # y luego escalado y traslación (centrar en la pantalla).
        # Posición relativa al Sol original: (body.pos[0] - sun_center_x, body.pos[1] - sun_center_y)
        # Posición escalada y centrada en la pantalla:
        draw_x = (body.pos[0] - sun_center_x) * scale_factor + offset_x
        draw_y = (body.pos[1] - sun_center_y) * scale_factor + offset_y

        # Calcular el radio escalado
        draw_radius = max(1, int(body.radius * scale_factor)) # Asegurarse de que el radio sea al menos 1 píxel

        # Dibujar el cuerpo celeste
        pygame.draw.circle(screen, body.color, (int(draw_x), int(draw_y)), draw_radius)

        # Opcional: Dibujar el nombre del cuerpo (simple)
        # font = pygame.font.Font(None, 15)
        # text = font.render(body.nombre, True, WHITE)
        # text_rect = text.get_rect(center=(int(draw_x), int(draw_y) - draw_radius - 5))
        # screen.blit(text, text_rect)


    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
sys.exit()