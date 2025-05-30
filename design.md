# Diseño Arquitectónico Inicial

Este documento describe el diseño arquitectónico inicial para el proyecto de simulación.

## 1. Estructura de Archivos/Módulos Propuesta

Se propone la siguiente estructura de archivos/módulos inicial:

*   `main.py`: Punto de entrada principal de la aplicación. Contendrá la lógica del bucle de simulación, inicialización y manejo de eventos generales.
*   `celestial_body.py`: Definición de la clase `CelestialBody` y posiblemente funciones relacionadas con cuerpos celestes (ej. cálculo de fuerzas gravitacionales).
*   `simulation.py` (Opcional, si la lógica del bucle principal se vuelve compleja): Podría encapsular la gestión de la simulación (lista de cuerpos, métodos de actualización).
*   `drawing.py` (Opcional, si la lógica de dibujo se vuelve compleja): Podría manejar la representación visual de los cuerpos y el sistema.
*   `constants.py` (Opcional): Para definir constantes globales (ej. constante gravitacional, unidades).

## 2. Definición de la Clase `CelestialBody`

La clase `CelestialBody` representará un cuerpo celeste individual en la simulación. Tendrá los siguientes atributos clave:

*   `nombre` (str): Nombre identificativo del cuerpo (ej. "Sol", "Tierra").
*   `masa` (float): Masa del cuerpo. Fundamental para el cálculo de la gravedad.
*   `radio` (float): Radio del cuerpo. Usado principalmente para la representación visual (tamaño en pantalla).
*   `color` (tuple/str): Color del cuerpo para el dibujo (ej. `(255, 255, 0)` para amarillo, "blue").
*   `posicion` (tuple/list/vector - (x, y)): Posición actual del centro del cuerpo en el sistema de coordenadas.
*   `velocidad` (tuple/list/vector - (vx, vy)): Velocidad actual del cuerpo en los ejes x e y.

Métodos potenciales (no especificados en la tarea, pero probables):
*   `update_position(dt)`: Actualiza la posición basándose en la velocidad y el paso de tiempo `dt`.
*   `update_velocity(acceleration, dt)`: Actualiza la velocidad basándose en la aceleración y el paso de tiempo `dt`.
*   `draw(screen)`: Dibuja el cuerpo en la superficie de la pantalla.

## 3. Sistema de Coordenadas

*   **Origen:** El origen `(0, 0)` del sistema de coordenadas se situará en el centro de la ventana de visualización.
*   **Unidades:** Las unidades físicas (masa, distancia, velocidad) se mantendrán consistentes (ej. kg, metros, m/s). La escala de visualización convertirá estas unidades físicas a píxeles.
*   **Escala:** Se definirá un factor de escala para mapear unidades físicas (metros) a píxeles en la pantalla. Por ejemplo, 1 unidad física = N píxeles. Este factor podrá ser ajustable. El eje Y positivo podría apuntar hacia arriba (matemático) o hacia abajo (convención de pantalla, a decidir).

## 4. Esbozo del Bucle Principal de Simulación

El bucle principal se ejecutará continuamente y gestionará el estado de la simulación y la visualización.

1.  **Inicialización:**
    *   Configurar la ventana de visualización.
    *   Inicializar los cuerpos celestes con sus atributos iniciales (posición, velocidad, masa, etc.).
    *   Configurar variables de simulación (paso de tiempo `dt`, escala, etc.).

2.  **Bucle de Eventos:**
    *   Manejar eventos del usuario (ej. cerrar ventana, entrada de teclado/ratón).

3.  **Actualización de Estado (Física):**
    *   Calcular las fuerzas que actúan sobre cada cuerpo (principalmente gravitación entre todos los pares de cuerpos).
    *   Calcular la aceleración resultante para cada cuerpo (`a = F/m`).
    *   Actualizar la velocidad de cada cuerpo basándose en su aceleración y el paso de tiempo `dt` (`v = v + a * dt`).
    *   Actualizar la posición de cada cuerpo basándose en su nueva velocidad y `dt` (`p = p + v * dt`).

4.  **Dibujo (Renderización):**
    *   Limpiar la pantalla (ej. rellenar con color de fondo).
    *   Para cada cuerpo celeste:
        *   Calcular su posición en píxeles basándose en su posición física y la escala.
        *   Dibujar el cuerpo (ej. un círculo) en la pantalla con su color y tamaño (radio escalado).
    *   Actualizar la pantalla para mostrar los cambios.

Este ciclo se repetirá para cada "frame" o paso de tiempo de la simulación.