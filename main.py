import pygame
from constants import *
from player import Player

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Create sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Set the containers for the Player class
    Player.containers = (updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update all sprites in the 'updatable' group
        updatable.update(dt)

        # Draw the game world
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        
        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
