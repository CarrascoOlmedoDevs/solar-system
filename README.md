# solar-system

## Descripción del Proyecto

`solar-system` es una aplicación interactiva desarrollada en Python utilizando la librería Pygame. Su objetivo es simular y visualizar el sistema solar, mostrando los planetas orbitando alrededor del sol y otros cuerpos celestes relevantes. La aplicación busca recrear el movimiento y la apariencia de los objetos celestes de la forma más realista posible dentro de las limitaciones de la simulación, permitiendo a los usuarios observar las dinámicas orbitales.

## Archivos Clave

*   **`main.py`**: Este es el punto de entrada principal de la aplicación. Contiene el bucle principal del juego, maneja los eventos de Pygame, actualiza el estado de los cuerpos celestes y coordina el renderizado de la escena. Es donde se inicializa la simulación y se gestiona la interacción del usuario.
*   **`celestial_body.py`**: Define la clase `CelestialBody`, que representa un objeto celeste individual (como un planeta, el sol, una luna, etc.). Esta clase encapsula propiedades como posición, velocidad, masa, radio y color, y contiene la lógica para calcular su movimiento orbital basado en las leyes de la gravedad (simulación N-body simplificada).

## Cómo Ejecutar

Para poner en marcha la aplicación `solar-system`, sigue los siguientes pasos:

1.  **Clonar el repositorio (si aplica):** Si el código fuente se encuentra en un repositorio de Git, clónalo a tu máquina local.
    ```bash
    git clone <url_del_repositorio> # Reemplaza con la URL real
    cd solar-system
    ```
2.  **Instalar dependencias:** La aplicación requiere la librería Pygame para funcionar. Puedes instalarla fácilmente usando pip, el gestor de paquetes de Python:
    ```bash
    pip install pygame
    ```
    Asegúrate de tener Python instalado en tu sistema.
3.  **Ejecutar la aplicación:** Una vez que hayas instalado Pygame, puedes ejecutar el archivo principal `main.py` desde la terminal:
    ```bash
    python main.py
    ```

Esto iniciará la ventana de Pygame y comenzará la simulación del sistema solar.