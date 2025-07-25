import pygame
from constants import *
from player import Player

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        # 1. Handle user input (events)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # 2. Draw the game world
        screen.fill("black")

        # Draw the player
        player.draw(screen)

        # 3. Update the display
        pygame.display.flip()

        # 4. Limit the frame rate and get delta time
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
