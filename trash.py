import pygame
import random
from config import *


class Trash(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # self.image = pygame.transform.scale(pygame.image.load())
        self.image = pygame.Surface((50, 50))
        self.image.fill((100, 100, 100))
        self.rect = self.image.get_rect(
            center=(WIN_WIDTH + 200, random.choice([200, 350, 500])))
