import pygame
from constants import *

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        # 1. Handle user input (events)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # 2. Draw the game world
        screen.fill("black")

        # 3. Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
