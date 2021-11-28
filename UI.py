import pygame
from config import *
from shark import Shark


class UI:
    pygame.font.init()
    font = pygame.font.Font("Assets/Fonts/slkscrb.ttf", 20)

    @classmethod
    def health_poison_bar_render(cls, shark: Shark):
        hp = cls.font.render("HP", True, (255, 255, 255))
        ps = cls.font.render("PS", False, (255, 255, 255))
        WINDOW_SURFACE.blit(hp, (20, 20))
        WINDOW_SURFACE.blit(ps, (20, 50))

        max_health_bar = pygame.Surface((200, 20))
        max_health_bar.fill((255, 255, 255))
        current_health_bar = pygame.Surface((200 * shark.health_ratio, 20))
        current_health_bar.fill((255, 0, 0))
        WINDOW_SURFACE.blit(max_health_bar, (60, 20))
        WINDOW_SURFACE.blit(current_health_bar, (60, 20))

        max_poison_bar = pygame.Surface((200, 20))
        max_poison_bar.fill((255, 255, 255))
        current_poison_bar = pygame.Surface((200 * shark.poison_ratio, 20))
        current_poison_bar.fill((0, 255, 0))
        WINDOW_SURFACE.blit(max_poison_bar, (60, 50))
        WINDOW_SURFACE.blit(current_poison_bar, (60, 50))
