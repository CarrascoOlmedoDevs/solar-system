import pygame
import sys
# Asegúrate de tener un archivo celestial_body.py con la clase CuerpoCeleste
# Asumimos que CuerpoCeleste ahora acepta un argumento 'parent' y 'has_rings'
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
sun_center_x = SCREEN_WIDTH // 2
sun_center_y = SCREEN_HEIGHT // 2

# Crear una instancia del Sol
# Nombre, masa (placeholder grande), radio, color, posición (vector), velocidad (vector), radio_orbital (0 para el sol), parent (None), has_rings (False)
# Usamos listas mutables para posición y velocidad
sun_pos = [float(sun_center_x), float(sun_center_y)] # Usar float para mayor precisión si se implementa física
sun_vel = [0.0, 0.0]
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
# Para órbitas circulares estables alrededor del Sol, la velocidad inicial v = sqrt(G*M_sol/r)
# Usaremos placeholders por ahora, pero la simulación N-body ajustará esto.
# Posición inicial: [sun_center_x + distancia, sun_center_y] (a la derecha del sol)
# Velocidad inicial placeholder: [0, -velocidad_placeholder] (hacia arriba para órbita anti-horaria)

# Placeholder para velocidades orbitales (magnitud)
# Estas son solo para dar una velocidad inicial. La simulación N-body real calculará la aceleración.
# Velocidades placeholders: Mercurio > Venus > Tierra > Marte > Júpiter > Saturno > Urano > Neptuno
vel_mercurio = 8
vel_venus = 7
vel_tierra = 6
vel_marte = 5
vel_jupiter = 4
vel_saturno = 3.5
vel_urano = 3
vel_neptuno = 2.5


mercurio_pos = [float(sun_center_x + distancia_mercurio), float(sun_center_y)]
mercurio_vel = [0.0, -vel_mercurio]
mercurio = CuerpoCeleste("Mercurio", 3.301e23, 4, GREY, mercurio_pos, mercurio_vel, distancia_mercurio, sun, False)
cuerpos_celestes.append(mercurio)

venus_pos = [float(sun_center_x + distancia_venus), float(sun_center_y)]
venus_vel = [0.0, -vel_venus]
venus = CuerpoCeleste("Venus", 4.867e24, 6, ORANGE, venus_pos, venus_vel, distancia_venus, sun, False)
cuerpos_celestes.append(venus)

tierra_pos = [float(sun_center_x + distancia_tierra), float(sun_center_y)]
tierra_vel = [0.0, -vel_tierra]
tierra = CuerpoCeleste("Tierra", 5.972e24, 8, BLUE, tierra_pos, tierra_vel, distancia_tierra, sun, False)
cuerpos_celestes.append(tierra)

marte_pos = [float(sun_center_x + distancia_marte), float(sun_center_y)]
marte_vel = [0.0, -vel_marte]
marte = CuerpoCeleste("Marte", 6.417e23, 5, RED, marte_pos, marte_vel, distancia_marte, sun, False)
cuerpos_celestes.append(marte)

jupiter_pos = [float(sun_center_x + distancia_jupiter), float(sun_center_y)]
jupiter_vel = [0.0, -vel_jupiter]
jupiter = CuerpoCeleste("Jupiter", 1.898e27, 15, BROWN, jupiter_pos, jupiter_vel, distancia_jupiter, sun, False)
cuerpos_celestes.append(jupiter)

saturno_pos = [float(sun_center_x + distancia_saturno), float(sun_center_y)]
saturno_vel = [0.0, -vel_saturno]
# Modificar Saturno para incluir anillos
saturno = CuerpoCeleste("Saturno", 5.683e26, 13, LIGHT_GREY, saturno_pos, saturno_vel, distancia_saturno, sun, True) # Añadimos has_rings=True
cuerpos_celestes.append(saturno)

urano_pos = [float(sun_center_x + distancia_urano), float(sun_center_y)]
urano_vel = [0.0, -vel_urano]
urano = CuerpoCeleste("Urano", 8.681e25, 10, LIGHT_BLUE, urano_pos, urano_vel, distancia_urano, sun, False)
cuerpos_celestes.append(urano)

neptuno_pos = [float(sun_center_x + distancia_neptuno), float(sun_center_y)]
neptuno_vel = [0.0, -vel_neptuno]
neptuno = CuerpoCeleste("Neptuno", 1.024e26, 10, DARK_BLUE, neptuno_pos, neptuno_vel, distancia_neptuno, sun, False)
cuerpos_celestes.append(neptuno)

# --- Crear instancias de Lunas ---
# Definir distancias orbitales relativas (en píxeles) desde el centro del planeta padre
# Y velocidades placeholders relativas al planeta padre

# Placeholder para velocidades orbitales de lunas (magnitud relativa)
# Estas son solo para dar una velocidad inicial. La simulación N-body real calculará la aceleración.
vel_luna_tierra = 8
vel_phobos = 10
vel_deimos = 9
vel_io = 7
vel_europa = 6
vel_ganymede = 5
vel_callisto = 4
vel_titan = 6


# Luna (de la Tierra)
distancia_luna = 20 # Distancia de la Tierra en píxeles
luna_pos = [float(tierra.pos[0] + distancia_luna), float(tierra.pos[1])] # Inicialmente a la derecha de la Tierra
luna_vel = [tierra.vel[0], tierra.vel[1] - vel_luna_tierra] # Velocidad inicial relativa a la Tierra
luna = CuerpoCeleste("Luna", 7.342e22, 3, GREY, luna_pos, luna_vel, distancia_luna, tierra, False)
cuerpos_celestes.append(luna)

# Lunas de Marte (Phobos y Deimos)
distancia_phobos = 10
phobos_pos = [float(marte.pos[0] + distancia_phobos), float(marte.pos[1])]
phobos_vel = [marte.vel[0], marte.vel[1] - vel_phobos]
phobos = CuerpoCeleste("Phobos", 1.06e16, 1, RED, phobos_pos, phobos_vel, distancia_phobos, marte, False)
cuerpos_celestes.append(phobos)

distancia_deimos = 15
deimos_pos = [float(marte.pos[0] - distancia_deimos), float(marte.pos[1])] # Inicialmente a la izquierda de Marte
deimos_vel = [marte.vel[0], marte.vel[1] + vel_deimos] # Velocidad inicial relativa a Marte (dirección opuesta)
deimos = CuerpoCeleste("Deimos", 1.47e15, 1, RED, deimos_pos, deimos_vel, distancia_deimos, marte, False)
cuerpos_celestes.append(deimos)

# Lunas Galileanas (de Jupiter)
distancia_io = 25
io_pos = [float(jupiter.pos[0] + distancia_io), float(jupiter.pos[1])]
io_vel = [jupiter.vel[0], jupiter.vel[1] - vel_io]
io = CuerpoCeleste("Io", 8.93e22, 4, LIGHT_ORANGE, io_pos, io_vel, distancia_io, jupiter, False)
cuerpos_celestes.append(io)

distancia_europa = 30
europa_pos = [float(jupiter.pos[0] - distancia_europa), float(jupiter.pos[1])]
europa_vel = [jupiter.vel[0], jupiter.vel[1] + vel_europa]
europa = CuerpoCeleste("Europa", 4.8e22, 4, LIGHT_BROWN, europa_pos, europa_vel, distancia_europa, jupiter, False)
cuerpos_celestes.append(europa)

distancia_ganymede = 38
ganymede_pos = [float(jupiter.pos[0]), float(jupiter.pos[1] + distancia_ganymede)] # Inicialmente debajo de Jupiter
ganymede_vel = [jupiter.vel[0] - vel_ganymede, jupiter.vel[1]] # Velocidad inicial relativa a Jupiter
ganymede = CuerpoCeleste("Ganymede", 1.48e23, 5, DARK_GREY, ganymede_pos, ganymede_vel, distancia_ganymede, jupiter, False)
cuerpos_celestes.append(ganymede)

distancia_callisto = 45
callisto_pos = [float(jupiter.pos[0]), float(jupiter.pos[1] - distancia_callisto)] # Inicialmente encima de Jupiter
callisto_vel = [jupiter.vel[0] + vel_callisto, jupiter.vel[1]] # Velocidad inicial relativa a Jupiter
callisto = CuerpoCeleste("Callisto", 1.08e23, 5, DARK_BROWN, callisto_pos, callisto_vel, distancia_callisto, jupiter, False)
cuerpos_celestes.append(callisto)

# Luna de Saturno (Titan)
distancia_titan = 25
titan_pos = [float(saturno.pos[0] + distancia_titan), float(saturno.pos[1])]
titan_vel = [saturno.vel[0], saturno.vel[1] - vel_titan]
titan = CuerpoCeleste("Titan", 1.35e23, 5, ORANGE, titan_pos, titan_vel, distancia_titan, saturno, False)
cuerpos_celestes.append(titan)


# Constante gravitacional (ajustada para la escala de la simulación si es necesario)
# G = 6.674e-11 # m^3 kg^-1 s^-2
# Para esta simulación visual, podemos usar una G ajustada para que las fuerzas sean visibles
# o simplemente usar los placeholders de velocidad y dejar que la física N-body se encargue.
# Si implementamos N-body real, esta G será importante.
# Por ahora, usamos una G simbólica si se calcula la fuerza, o confiamos en las velocidades iniciales.
G = 0.00000000006674 # Placeholder, podría necesitar ajuste drástico para la escala de píxeles/tiempo

# Factor de escala para visualizar distancias (no se usa directamente para la física N-body,
# pero ayuda a entender las distancias relativas iniciales)
# max_orbital_radius = distancia_neptuno
# scale_factor = (SCREEN_WIDTH / 2) / max_orbital_radius # Escalar para que Neptuno quepa

# Variable para controlar el estado de ejecución del juego
running = True

# Bucle principal del juego
while running:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Lógica de actualización (Simulación N-body) ---
    # Calcular fuerzas gravitacionales entre todos los pares de cuerpos
    # Esto es computacionalmente intensivo (O(n^2))
    # En una simulación real, se calcularía la aceleración de cada cuerpo
    # debido a la suma vectorial de las fuerzas de todos los demás cuerpos.
    # Luego se actualizaría la velocidad y posición usando métodos de integración numérica (ej: Euler, Verlet).

    # Para esta versión simple, solo actualizaremos posiciones/velocidades si la física N-body está implementada
    # Si no, simplemente se moverán con sus velocidades iniciales o se mantendrán estáticos.
    # Asumimos que la lógica de actualización está o será implementada en CuerpoCeleste.update()
    # o en una función separada que itera sobre cuerpos_celestes.

    # Ejemplo básico de actualización (requiere implementación en CuerpoCeleste.update)
    # for body in cuerpos_celestes:
    #     body.update(cuerpos_celestes, G, timestep) # timestep es el paso de tiempo de la simulación

    # --- Dibujar ---
    # Rellenar el fondo de negro
    screen.fill(BLACK)

    # Dibujar cada cuerpo celeste
    for body in cuerpos_celestes:
        # La posición almacenada en body.pos es la posición "real" en el sistema de coordenadas de la simulación
        # Necesitamos convertir esta posición a coordenadas de pantalla si la simulación usa una escala/origen diferente
        # En este setup inicial, body.pos ya está en coordenadas de pantalla centradas en el Sol.

        # Dibujar el cuerpo
        body.draw(screen)

        # Opcional: Dibujar órbita (si estuviera implementado)
        # if body.orbital_radius > 0:
        #     # Calcular la posición del centro de la órbita (asumimos que es el padre o el Sol)
        #     center_pos = body.parent.pos if body.parent else sun.pos
        #     # Dibujar un círculo
        #     pygame.draw.circle(screen, WHITE, (int(center_pos[0]), int(center_pos[1])), int(body.orbital_radius), 1)


    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de fotogramas (opcional)
    # pygame.time.Clock().tick(60) # Limita a 60 FPS

# Salir de Pygame
pygame.quit()
sys.exit()