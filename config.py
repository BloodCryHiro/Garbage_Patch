import pygame
from pygame.surface import Surface

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIN_WIDTH = 800
WIN_HEIGHT = 600
WINDOW_SURFACE = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

SPAWN = pygame.USEREVENT + 1
ENTER_GAME = pygame.USEREVENT + 2
GAME_OVER = pygame.USEREVENT + 3
RESTART_GAME = pygame.USEREVENT + 4


def center(outer: Surface, inner: Surface):
    return ((outer.get_width() - inner.get_width()) / 2, (outer.get_height() - inner.get_height()) / 2)
