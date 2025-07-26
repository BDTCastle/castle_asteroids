import pygame
from circleshape import CircleShape

class Particle(CircleShape):
    def __init__(self, x, y, radius, lifespan):
        super().__init__(x, y, radius)
        self.lifespan = lifespan

    def update(self, dt):
        super().update(dt) # This handles movement and screen wrapping
        self.lifespan -= dt
        if self.lifespan <= 0:
            self.kill()

    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", self.position, self.radius)