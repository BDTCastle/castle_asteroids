import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0
        self.invincibility_timer = PLAYER_INVINCIBILITY_TIME
        self.speed_boost_timer = 0
        self.acceleration = PLAYER_ACCELERATION

    def reset(self):
        self.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.velocity = pygame.Vector2(0, 0)
        self.invincibility_timer = PLAYER_INVINCIBILITY_TIME


    def activate_speed_boost(self):
        self.speed_boost_timer = 5.0 # 5 seconds of boost
        self.acceleration = PLAYER_ACCELERATION * 2

    def accelerate(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.velocity += forward * self.acceleration * dt

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def shoot(self):
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y)
        velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        shot.velocity = velocity

    def update(self, dt):

        # --- NEW: Speed boost timer ---
        if self.speed_boost_timer > 0:
            self.speed_boost_timer -= dt
            if self.speed_boost_timer <= 0:
                self.acceleration = PLAYER_ACCELERATION # Reset to normal
        # Timers
        self.shoot_timer -= dt
        self.invincibility_timer -= dt
        if self.speed_boost_timer > 0:
            self.speed_boost_timer -= dt
            if self.speed_boost_timer <= 0:
                self.acceleration = PLAYER_ACCELERATION
        
        # Physics
        self.velocity *= PLAYER_FRICTION
        super().update(dt) # This handles movement and screen wrapping

        # --- Mouse Aiming ---
        mouse_pos = pygame.mouse.get_pos()
        direction_vector = pygame.Vector2(mouse_pos) - self.position
        self.rotation = pygame.Vector2(0, 1).angle_to(direction_vector)

        # Input
        keys = pygame.key.get_pressed()
        right_vector = pygame.Vector2(0, 1).rotate(self.rotation + 90)
        if keys[pygame.K_a]: # Strafe Left
            self.velocity -= right_vector * self.acceleration * dt * 0.5
        if keys[pygame.K_d]: # Strafe Right
            self.velocity += right_vector * self.acceleration * dt * 0.5
        if keys[pygame.K_w]:
            self.accelerate(dt)
        if keys[pygame.K_s]:
            self.accelerate(-dt)

    def draw(self, screen):
        # Change color based on invincibility
        if self.invincibility_timer > 0:
            color = "yellow"
        else:
            color = "white"
        
        pygame.draw.polygon(screen, color, self.triangle(), 2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]