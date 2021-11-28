import pygame

WHITE = (255, 255, 255)

WIN_WIDTH = 800
WIN_HEIGHT = 600
WINDOW_SURFACE = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

SPAWN = pygame.USEREVENT + 1
GAME_OVER = pygame.USEREVENT + 2
