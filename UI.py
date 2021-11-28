import pygame
from config import *
from shark import Shark


class UI:
    pygame.font.init()

    @classmethod
    def display_health_poison_bar(cls, shark: Shark):
        bar_font = pygame.font.Font("Assets/Fonts/slkscre.ttf", 20)
        hp = bar_font.render("HP", True, WHITE)
        ps = bar_font.render("PS", False, WHITE)
        WINDOW_SURFACE.blit(hp, (20, 20))
        WINDOW_SURFACE.blit(ps, (20, 50))

        max_health_bar = pygame.Surface((200, 20))
        max_health_bar.fill(WHITE)
        current_health_bar = pygame.Surface((200 * shark.health_ratio, 20))
        current_health_bar.fill((255, 0, 0))
        WINDOW_SURFACE.blit(max_health_bar, (60, 20))
        WINDOW_SURFACE.blit(current_health_bar, (60, 20))

        max_poison_bar = pygame.Surface((200, 20))
        max_poison_bar.fill(WHITE)
        current_poison_bar = pygame.Surface((200 * shark.poison_ratio, 20))
        current_poison_bar.fill((0, 255, 0))
        WINDOW_SURFACE.blit(max_poison_bar, (60, 50))
        WINDOW_SURFACE.blit(current_poison_bar, (60, 50))

    score = 0

    @classmethod
    def display_score(cls):
        score_font = pygame.font.Font("Assets/Fonts/slkscre.ttf", 30)
        score_word = score_font.render(
            f"Score: {str(cls.score)}", True, WHITE)
        WINDOW_SURFACE.blit(score_word, (WIN_WIDTH - 220, 25))

    time_count = 0

    @classmethod
    def timer(cls):
        cls.time_count += 1
        if cls.time_count == 60:
            cls.time_count = 0
            cls.score += 1
