import pygame
import random
import math
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, SCORE_SMALL, SCORE_MEDIUM, SCORE_LARGE
from particle import Particle
from powerup import ShieldPowerUp, SpeedPowerUp

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.vertices = []
        num_vertices = random.randint(8, 12)
        for i in range(num_vertices):
            angle = (i / num_vertices) * 2 * math.pi
            # Vary the distance from the center to make it "lumpy"
            dist = self.radius + random.uniform(-self.radius / 4, self.radius / 4)
            vx = dist * math.cos(angle)
            vy = dist * math.sin(angle)
            self.vertices.append((vx, vy))

    def split(self):
        self.kill()
        for _ in range(10):
            particle = Particle(self.position.x, self.position.y, 2, 1.0)
            angle = random.uniform(0, 360)
            speed = random.uniform(50, 150)
            particle.velocity = pygame.Vector2(0, 1).rotate(angle) * speed

        if random.random() < 0.1:
            powerup_class = random.choice([ShieldPowerUp, SpeedPowerUp])
            powerup = powerup_class(self.position.x, self.position.y)

        if self.radius <= ASTEROID_MIN_RADIUS:
            return SCORE_SMALL
        elif self.radius <= ASTEROID_MIN_RADIUS * 2:
            score = SCORE_MEDIUM
        else:
            score = SCORE_LARGE

        angle = random.uniform(20, 50)
        vel1 = self.velocity.rotate(angle)
        vel2 = self.velocity.rotate(-angle)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = vel1 * 1.2
        
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = vel2 * 1.2
        
        return score

    def draw(self, screen):
        screen_points = [(p[0] + self.position.x, p[1] + self.position.y) for p in self.vertices]
        pygame.draw.polygon(screen, "white", screen_points, 2)

    def update(self, dt):
        super().update(dt)