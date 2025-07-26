import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from particle import Particle
from powerup import ShieldPowerUp, SpeedPowerUp

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Create sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    particles = pygame.sprite.Group()
    powerups = pygame.sprite.Group()

    # Set the containers for the Player class
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Particle.containers = (particles, updatable, drawable)
    AsteroidField.containers = (updatable,)
    # The containers for the children must be set
    ShieldPowerUp.containers = (powerups, updatable, drawable)
    SpeedPowerUp.containers = (powerups, updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # Score and life keeping
    score = 0
    lives = 3
    font = pygame.font.Font(None, 40)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if player.shoot_timer <= 0:
                    player.shoot()    

        # Update all sprites in the 'updatable' group
        updatable.update(dt)

        # Check for collisions
        for asteroid in asteroids:
            # --- THIS LINE IS CHANGED ---
            if player.invincibility_timer <= 0 and player.collides_with(asteroid):
                lives -= 1
                if lives > 0:
                    asteroid.kill()
                    player.reset()
                else:
                    print(f"Game over! Final Score: {score}")
                    return
                
        # --- Player vs Power-ups ---
        collided_powerups = pygame.sprite.spritecollide(player, powerups, True)
        for powerup in collided_powerups:
            powerup.apply_to_player(player)

        # Shots vs Asteroids
        for shot in shots:
            for asteroid in asteroids:
                if shot.collides_with(asteroid):
                    shot.kill()
                    asteroid.split() # This line is changed
                     # This line adds the returned value to the score
                    score += asteroid.split()

        # Draw the game world
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        
        # Draw score and lives
        score_text = font.render(f"Score: {score}", True, "white")
        screen.blit(score_text, (10, 10))
        lives_text = font.render(f"Lives: {lives}", True, "white")
        screen.blit(lives_text, (SCREEN_WIDTH - 150, 10))
            
        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
