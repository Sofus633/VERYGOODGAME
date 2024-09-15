import pygame
import sys

class Vector2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Vector2(self.x / scalar, self.y / scalar)

    def magnitude(self):
        return (self.x**2 + self.y**2) ** 0.5

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            return Vector2(0, 0)
        return self / mag

    def limit(self, max_value):
        if self.magnitude() > max_value:
            return self.normalize() * max_value
        return self

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Movement with Vectors and Deceleration")

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Initial position, velocity, and parameters
position = Vector2(screen_width // 2, screen_height // 2)
velocity = Vector2(0, 0)
speed = 5
deceleration = 0.95  # Deceleration factor to gradually reduce velocity

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys pressed
    keys = pygame.key.get_pressed()

    # Update velocity based on key inputs
    if keys[pygame.K_LEFT]:
        velocity.x = -speed
    if keys[pygame.K_RIGHT]:
        velocity.x = speed
    else:
        # Apply deceleration
        velocity.x *= deceleration

    if keys[pygame.K_UP]:
        velocity.y = -speed
    if keys[pygame.K_DOWN]:
        velocity.y = speed
    else:
        # Apply deceleration
        velocity.y *= deceleration

    # Update position using velocity
    position += velocity

    # Clear the screen
    screen.fill(WHITE)

    # Draw the object (a blue rectangle)
    pygame.draw.rect(screen, BLUE, (int(position.x), int(position.y), 50, 50))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate at 60 FPS
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
