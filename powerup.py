import pygame
from circleshape import CircleShape
from constants import PLAYER_INVINCIBILITY_TIME, PLAYER_ACCELERATION

# Base class for all power-ups
class PowerUp(CircleShape):
    def __init__(self, x, y, radius, lifespan):
        super().__init__(x, y, radius)
        self.lifespan = lifespan

    def update(self, dt):
        super().update(dt)
        self.lifespan -= dt
        if self.lifespan <= 0:
            self.kill()

    def apply_to_player(self, player):
        # Child classes must implement this
        raise NotImplementedError

# Shield Power-Up
class ShieldPowerUp(PowerUp):
    def __init__(self, x, y):
        super().__init__(x, y, 15, 5.0) # 15px radius, 5-second lifespan

    def draw(self, screen):
        pygame.draw.circle(screen, "cyan", self.position, self.radius, 3)

    def apply_to_player(self, player):
        player.invincibility_timer = PLAYER_INVINCIBILITY_TIME

# Speed Boost Power-Up
class SpeedPowerUp(PowerUp):
    def __init__(self, x, y):
        super().__init__(x, y, 15, 5.0) # 15px radius, 5-second lifespan

    def draw(self, screen):
        # Simple representation of a speed boost (e.g., green chevrons)
        p1 = self.position + pygame.Vector2(0, -self.radius)
        p2 = self.position + pygame.Vector2(-self.radius / 2, 0)
        p3 = self.position + pygame.Vector2(self.radius / 2, 0)
        pygame.draw.polygon(screen, "green", [p1, p2, p3], 3)
        
    def apply_to_player(self, player):
        player.activate_speed_boost()