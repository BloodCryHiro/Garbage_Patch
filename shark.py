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
        self.poison_timer = 0

    def movement(self, pressed_key):
        if pressed_key[pygame.K_UP] and not self.rect.center == (150, 200):
            self.rect.y -= 150
        elif pressed_key[pygame.K_DOWN] and not self.rect.center == (150, 500):
            self.rect.y += 150

    def collision(self, target):
        if target == "trash":
            # ! temp
            self.current_health -= 100
            self.current_poison += 10
        if target == "normal":
            if self.current_health + 5 <= 100:
                self.current_health += 5
            self.current_poison += 5
        if target == "poisoned":
            self.current_poison += 15
        self.health_ratio = self.current_health / self.max_health
        self.poison_ratio = self.current_poison / self.max_poison

    def poison_decay(self):
        self.poison_timer += 1
        if self.poison_timer == 120:
            self.poison_timer = 0
            if self.current_poison - 1 >= 0:
                self.current_poison -= 1
                self.poison_ratio = self.current_poison / self.max_poison

    def death(self):
        if self.current_health <= 0 or self.current_poison >= 100:
            pygame.event.post(pygame.event.Event(GAME_OVER))

    def restart(self):
        self.current_health = 100
        self.health_ratio = self.current_health / self.max_health
        self.current_poison = 0
        self.poison_ratio = self.current_poison / self.max_poison

    def update(self):
        self.poison_decay()
        self.death()
