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
WHITE = (255, 255, 255) # Color para las órbitas
YELLOW = (255, 255, 0)
GREY = (150, 150, 150)
ORANGE = (255, 165, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BROWN = (139, 69, 19) # Para Jupiter quizás
LIGHT_BLUE = (173, 216, 230) # Para Urano quizás
DARK_BLUE = (0, 0, 139) # Para Neptuno quizás
LIGHT_GREY = (200, 200, 200) # Para Saturno quizás

# Crear la superficie de visualización (ventana)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Establecer el título de la ventana
pygame.display.set_caption("Sistema Solar Simple con Gravedad N-body")

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
# La masa del sol es mucho mayor que la de los planetas
sun = CuerpoCeleste("Sol", 1.989e30, 20, YELLOW, sun_pos, sun_vel, 0) # El sol no tiene órbita alrededor de sí mismo
cuerpos_celestes.append(sun)

# Crear instancias de los planetas interiores
# Definir distancias orbitales relativas (en píxeles)
# Estas son distancias iniciales desde el centro del Sol
distancia_mercurio = 50
distancia_venus = 80
distancia_tierra = 120
distancia_marte = 180

# Las velocidades iniciales se establecen tangenciales a la órbita inicial
# y con magnitudes placeholder. La física real se añadiría en la lógica de actualización.
# Para órbitas circulares estables, la velocidad inicial v = sqrt(G*M/r) donde M es la masa del cuerpo central (Sol)
# y r es la distancia orbital. Usaremos placeholders por ahora, pero la simulación N-body ajustará esto.
# Posición inicial: [sun_center_x + distancia, sun_center_y] (a la derecha del sol)
# Velocidad inicial placeholder: [0, -velocidad_placeholder] (hacia arriba para órbita anti-horaria simple)

# Mercurio
mercury_orbital_radius = distancia_mercurio
mercury_pos = [float(sun_center_x + mercury_orbital_radius), float(sun_center_y)]
# Velocidad inicial placeholder (ajustar G_SCALED y estas velocidades para órbitas más estables)
# v_placeholder = math.sqrt(G_SCALED * sun.masa / mercury_orbital_radius) # Cálculo teórico para órbita circular
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
marte_orbital_radius = distancia_marte
marte_pos = [float(sun_center_x + marte_orbital_radius), float(sun_center_y)]
marte_vel = [0.0, -3.0] # Placeholder
marte = CuerpoCeleste("Marte", 0.642e24, 5, RED, marte_pos, marte_vel, marte_orbital_radius)
cuerpos_celestes.append(marte)

# Crear instancias de los planetas exteriores (con distancias mayores)
distancia_jupiter = 250
distancia_saturno = 320
distancia_urano = 380
distancia_neptuno = 420

# Jupiter
jupiter_orbital_radius = distancia_jupiter
jupiter_pos = [float(sun_center_x + jupiter_orbital_radius), float(sun_center_y)]
jupiter_vel = [0.0, -2.0] # Placeholder
# Masa de Jupiter es mucho mayor que los interiores
jupiter = CuerpoCeleste("Jupiter", 1898e24, 15, BROWN, jupiter_pos, jupiter_vel, jupiter_orbital_radius)
cuerpos_celestes.append(jupiter)

# Saturno
saturno_orbital_radius = distancia_saturno
saturno_pos = [float(sun_center_x + saturno_orbital_radius), float(sun_center_y)]
saturno_vel = [0.0, -1.5] # Placeholder
saturno = CuerpoCeleste("Saturno", 568e24, 12, LIGHT_GREY, saturno_pos, saturno_vel, saturno_orbital_radius)
cuerpos_celestes.append(saturno)

# Urano
urano_orbital_radius = distancia_urano
urano_pos = [float(sun_center_x + urano_orbital_radius), float(sun_center_y)]
urano_vel = [0.0, -1.0] # Placeholder
urano = CuerpoCeleste("Urano", 86.8e24, 10, LIGHT_BLUE, urano_pos, urano_vel, urano_orbital_radius)
cuerpos_celestes.append(urano)

# Neptuno
neptuno_orbital_radius = distancia_neptuno
neptuno_pos = [float(sun_center_x + neptuno_orbital_radius), float(sun_center_y)]
neptuno_vel = [0.0, -0.8] # Placeholder
neptuno = CuerpoCeleste("Neptuno", 102e24, 10, DARK_BLUE, neptuno_pos, neptuno_vel, neptuno_orbital_radius)
cuerpos_celestes.append(neptuno)


# --- Bucle principal del juego ---
running = True
clock = pygame.time.Clock() # Inicializar el objeto Clock para controlar el tiempo
FPS = 60 # Frames por segundo

# Constante gravitacional escalada para la simulación en píxeles
# Este valor necesita ser ajustado experimentalmente para obtener órbitas visualmente estables
# Un valor muy pequeño resultará en poca interacción, un valor muy grande en caos o eyección.
G_SCALED = 0.00000000002 # Ajustar este valor! Las masas son grandes, G debe ser muy pequeña.
# Si las masas fueran escaladas (ej. masa_real / 1e24), G podría ser más grande (ej. 6.674e-11 * 1e-24 * factor_pixel_a_metro_cuadrado)
# Probemos con masas originales y un G muy pequeño, o escalemos las masas.
# Escalar masas parece más intuitivo: dividimos las masas reales por un factor grande.
MASS_SCALE_FACTOR = 1e24 # Dividir todas las masas por este factor
G_ACTUAL = 6.674e-11 # N(m/kg)^2
# Necesitamos G_sim = G_actual * (masa_real / masa_sim) * (distancia_sim / distancia_real)^2 / tiempo_sim^2
# Si masa_sim = masa_real / MASS_SCALE_FACTOR, distancia_sim = distancia_pixel, tiempo_sim = dt (segundos)
# G_sim = G_actual * MASS_SCALE_FACTOR * (pixel_to_meter)^2
# Si 1 pixel = 1e9 metros (ej. 1 AU ~ 150M km = 1.5e11 m, si 120px = 1 AU, 1px = 1.25e9 m)
# factor_pixel_a_metro = 1.25e9
# G_SCALED = G_ACTUAL * MASS_SCALE_FACTOR * (factor_pixel_a_metro)**2
# G_SCALED = 6.674e-11 * 1e24 * (1.25e9)**2 = 6.674e13 * 1.5625e18 = 1.04e32 -> ¡Demasiado grande!

# Es más simple ajustar G_SCALED empíricamente o escalar masas y G juntas.
# Opción 1: Mantener masas reales, ajustar G_SCALED empíricamente (probado arriba, valores muy pequeños)
# G_SCALED = 0.00000000002 # Todavía parece muy pequeño.

# Opción 2: Escalar masas y ajustar G_SCALED.
# Vamos a dividir las masas por 1e24 (ya lo hicimos en la creación de objetos).
# Ahora G_sim = G_actual * factor_distancia^2. Si 1 pixel = 1e9 metros (aproximación)
# G_SCALED = 6.674e-11 * (1e9)^2 = 6.674e-11 * 1e18 = 6.674e7. Todavía grande.

# Opción 3: Ajustar G_SCALED empíricamente con masas escaladas.
# Las masas ahora están en unidades de 10^24 kg. El sol es ~1989 unidades.
# Las distancias están en píxeles.
# Necesitamos F = G_SCALED * m1_scaled * m2_scaled / r_pixels^2
# F = m_scaled * a
# a = G_SCALED * m2_scaled / r_pixels^2
# v += a * dt
# p += v * dt
# Si a es del orden de 1 pixel/seg^2, y m2_scaled es del orden de 1 (para planetas), r_pixels es del orden de 100.
# 1 ~ G_SCALED * 1 / 100^2 => G_SCALED ~ 10000.
# Si a es del orden de 100 pixels/seg^2 (para el sol), y m_sol_scaled ~ 2000, r_pixels ~ 100.
# 100 ~ G_SCALED * 2000 / 100^2 => G_SCALED ~ 100 * 10000 / 2000 = 1000000 / 2000 = 500.
# Probemos un G_SCALED en este rango.
G_SCALED = 500 # Valor empírico, ajustar según necesites que se muevan los planetas.

# Escalar masas al crear los objetos para usar G_SCALED más manejable
# Ya lo hicimos al definir las masas como 1.989e30, 0.330e24, etc.
# Si queremos usar las masas como 1989, 0.330, etc., debemos dividir por 1e27 o 1e24.
# Vamos a dividir por 1e24 para que las masas de los planetas interiores sean < 1.
# Sun: 1.989e30 / 1e24 = 1.989e6
# Mercury: 0.330e24 / 1e24 = 0.330
# Venus: 4.867e24 / 1e24 = 4.867
# Earth: 5.972e24 / 1e24 = 5.972
# Mars: 0.642e24 / 1e24 = 0.642
# Jupiter: 1898e24 / 1e24 = 1898
# Saturn: 568e24 / 1e24 = 568
# Uranus: 86.8e24 / 1e24 = 86.8
# Neptune: 102e24 / 1e24 = 102
# Con estas masas escaladas, G_SCALED = 0.005 podría ser un buen punto de partida (basado en pruebas empíricas con simulaciones similares).

# Re-crear cuerpos con masas escaladas
cuerpos_celestes = [] # Limpiar la lista
sun = CuerpoCeleste("Sol", 1.989e6, 20, YELLOW, sun_pos, sun_vel, 0) # Masa escalada
cuerpos_celestes.append(sun)

mercury_pos = [float(sun_center_x + distancia_mercurio), float(sun_center_y)]
mercury_vel = [0.0, -math.sqrt(G_SCALED * sun.masa / distancia_mercurio)] # Velocidad inicial para órbita circular
mercury = CuerpoCeleste("Mercurio", 0.330, 3, GREY, mercury_pos, mercury_vel, distancia_mercurio) # Masa escalada
cuerpos_celestes.append(mercury)

venus_pos = [float(sun_center_x + distancia_venus), float(sun_center_y)]
venus_vel = [0.0, -math.sqrt(G