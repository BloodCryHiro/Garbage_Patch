import pygame
import random
from config import *


class NormalFish(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load("Assets/Arts/fish.png"), (50, 25))
        self.rect = self.image.get_rect(
            center=(WIN_WIDTH + 200, random.choice([200, 350, 500])))


class PoisonedFish(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load("Assets/Arts/green_fish.png"), (50, 25))
        self.rect = self.image.get_rect(
            center=(WIN_WIDTH + 200, random.choice([200, 350, 500])))
