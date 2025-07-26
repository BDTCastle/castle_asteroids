import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        self.rect = pygame.Rect(x, y, radius * 2, radius * 2)

    def collides_with(self, other):
        distance = self.position.distance_to(other.position)
        return distance <= self.radius + other.radius
    
    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # Move the object
        self.position += self.velocity * dt

        self.rect.center = self.position

        # Wrap the object around the screen
        if self.position.x > SCREEN_WIDTH:
            self.position.x = 0
        if self.position.x < 0:
            self.position.x = SCREEN_WIDTH
        if self.position.y > SCREEN_HEIGHT:
            self.position.y = 0
        if self.position.y < 0:
            self.position.y = SCREEN_HEIGHT