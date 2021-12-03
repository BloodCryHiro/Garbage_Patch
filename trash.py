import pygame
import random
from config import *


class Trash(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load(random.choice(["Assets/Arts/trash_1.png", "Assets/Arts/trash_2.png", "Assets/Arts/trash_3.png"])), (50, 50))
        self.rect = self.image.get_rect(
            center=(WIN_WIDTH + 200, random.choice([200, 350, 500])))
