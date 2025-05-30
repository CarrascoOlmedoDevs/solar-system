# Research Summary: Pygame Simulation

## Pygame Concepts to Use

*   **Initialization and Shutdown:** `pygame.init()`, `pygame.quit()`.
*   **Game Loop:** Main loop structure (`while running:`).
*   **Event Handling:** Processing user input (e.g., `pygame.event.get()`, `pygame.QUIT`).
*   **Display Surface:** Creating the window (`pygame.display.set_mode()`).
*   **Drawing:** Using drawing primitives or surfaces (`surface.fill()`, `pygame.draw.circle()`, `surface.blit()`).
*   **Clock:** Controlling frame rate (`pygame.time.Clock()`, `clock.tick()`).
*   **Vectors:** Potentially use `pygame.math.Vector2` for position, velocity, and acceleration.

## Initial Physics Approach

*   **Simplified Newtonian Gravity:** Implement gravitational force between objects.
    *   Force is proportional to the product of masses and inversely proportional to the square of the distance.
    *   F = G * (m1 * m2) / r^2
    *   G will likely be a tunable constant, not necessarily the real gravitational constant, to control simulation speed/scale.
*   **Integration:** Use simple Euler integration for updating velocity and position based on acceleration (derived from forces).
    *   `velocity += acceleration * dt`
    *   `position += velocity * dt`
    *   `dt` is the time delta provided by the clock.
*   **No Collisions (Initial):** Collision detection and response will be ignored in the initial phase to focus on gravitational dynamics.

## Coordinate System Decisions

*   **Origin:** Top-left corner of the display window (standard Pygame convention).
*   **Axes Orientation:**
    *   X-axis: Positive to the right.
    *   Y-axis: Positive downwards (standard Pygame convention).
*   **Units:** Coordinates will be in pixels. Physics calculations (position, velocity, acceleration) will need to account for this pixel-based system. Masses will be abstract units. G will bridge these units.