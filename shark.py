import pygame
from pygame.math import enable_swizzling
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

    def collision(self, target):
        if target == "trash":
            if self.current_poison - 10 <= 0 or self.current_poison + 10 >= 100:
                pygame.event.post(pygame.event.Event(GAME_OVER))
            else:
                self.current_health -= 10
                self.current_poison += 10
        if target == "normal":
            if self.current_poison + 15 >= 100:
                pygame.event.post(pygame.event.Event(GAME_OVER))
            else:
                if self.current_health + 5 <= 100:
                    self.current_health += 5
                self.current_poison += 5
        if target == "poisoned":
            if self.current_poison + 15 >= 100:
                pygame.event.post(pygame.event.Event(GAME_OVER))
            else:
                self.current_poison += 15
        self.health_ratio = self.current_health / self.max_health
        self.poison_ratio = self.current_poison / self.max_poison
