import pygame
from config import *


def main():
    pygame.init()
    pygame.display.set_caption("Garbage Patch")
    window_surface = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    isRunning = True
    while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False

    pygame.quit()


if __name__ == "__main__":
    main()
