import pygame
from config import *


class Shark(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load("Assets/Arts/shark.png"), (100, 50))
        self.rect = self.image.get_rect(center=(150, 350))

        self.max_health = 100
        self.current_health = 100
        self.health_ratio = self.current_health / self.max_health
        self.max_poison = 100
        self.current_poison = 0
        self.poison_ratio = self.current_poison / self.max_poison

    def movement(self, pressed_key):
        if pressed_key[pygame.K_UP] and not self.rect.center == (150, 200):
            self.rect.y -= 150
        elif pressed_key[pygame.K_DOWN] and not self.rect.center == (150, 500):
            self.rect.y += 150
