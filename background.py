import pygame
from config import *


class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_1 = pygame.transform.scale(pygame.image.load(
            "Assets/Arts/background.png"), (WIN_WIDTH, WIN_HEIGHT))
        self.image_2 = pygame.transform.scale(pygame.image.load(
            "Assets/Arts/background_test.png"), (WIN_WIDTH, WIN_HEIGHT))
        self.image = pygame.Surface((WIN_WIDTH * 2, WIN_HEIGHT))
        self.image.blit(self.image_1, (WIN_WIDTH, 0))
        self.image.blit(self.image_2, (0, 0))
        self.rect = self.image.get_rect(midtop=(0, 0))
