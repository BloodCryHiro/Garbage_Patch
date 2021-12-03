import pygame
from config import *
from shark import Shark


class Button:
    buttons_list = []

    def __init__(self, background_color, background_size, background_position, font_size, content, font_color):
        self.background_color = background_color
        self.background_rect = pygame.Rect(
            background_position, background_size)

        self.content = content
        self.font = pygame.font.Font("Assets/Fonts/slkscre.ttf", font_size)
        self.word = self.font.render(content, True, font_color)
        self.word_rect = self.word.get_rect(center=self.background_rect.center)

        Button.buttons_list.append(self)

    def draw(self):
        pygame.draw.rect(WINDOW_SURFACE, self.background_color,
                         self.background_rect)
        WINDOW_SURFACE.blit(self.word, self.word_rect)

    def click(self, mouse_position):
        if self.background_rect.collidepoint(mouse_position):
            if self.content == "Start":
                pygame.event.post(pygame.event.Event(ENTER_GAME))
            elif self.content == "Exit":
                pygame.event.post(pygame.event.Event(pygame.QUIT))
            elif self.content == "Restart":
                pygame.event.post(pygame.event.Event(RESTART_GAME))


class UI:
    pygame.font.init()

    score = 0

    point_time_count = 0

    @ classmethod
    def display_health_poison_bar(cls, shark: Shark):
        bar_font = pygame.font.Font("Assets/Fonts/slkscre.ttf", 20)
        hp = bar_font.render("HP", True, WHITE)
        ps = bar_font.render("PS", True, WHITE)
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

    @ classmethod
    def display_score(cls):
        score_font = pygame.font.Font("Assets/Fonts/slkscre.ttf", 30)
        score_word = score_font.render(
            f"Score: {str(cls.score)}", True, WHITE)
        WINDOW_SURFACE.blit(score_word, (WIN_WIDTH - 220, 25))

    @ classmethod
    def point_timer(cls):
        cls.point_time_count += 1
        if cls.point_time_count == 60:
            cls.point_time_count = 0
            cls.score += 1

    @ classmethod
    def start_menu(cls):
        background = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
        background.fill((50, 50, 50))
        WINDOW_SURFACE.blit(background, (0, 0))

        game_title_font = pygame.font.Font("Assets/Fonts/slkscre.ttf", 50)
        game_title_word = game_title_font.render(
            "Garbage Overflow", True, WHITE)
        WINDOW_SURFACE.blit(game_title_word, (WIN_WIDTH / 2 - game_title_word.get_width() /
                            2, 150))

        start_button = Button(WHITE, (game_title_word.get_width() * 0.7, 40), ((
            WIN_WIDTH - game_title_word.get_width() * 0.7) / 2, WIN_HEIGHT / 2), 30, "Start", BLACK)
        start_button.draw()

        exit_button = Button(WHITE, (game_title_word.get_width(
        ) * 0.7, 40), (start_button.background_rect.x, start_button.background_rect.y + 60), 30, "Exit", BLACK)
        exit_button.draw()

        pygame.display.update()

    @ classmethod
    def game_over(cls):
        background = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
        background.fill((50, 50, 50))
        WINDOW_SURFACE.blit(background, (0, 0))

        game_over_font = pygame.font.Font("Assets/Fonts/slkscre.ttf", 50)
        game_over_word = game_over_font.render("Game Over", True, WHITE)
        WINDOW_SURFACE.blit(game_over_word, (WIN_WIDTH / 2 - game_over_word.get_width() /
                            2, 150))

        restart_button = Button(WHITE, (game_over_word.get_width() * 0.7, 40), ((
            WIN_WIDTH - game_over_word.get_width() * 0.7) / 2, WIN_HEIGHT / 2), 30, "Restart", BLACK)
        restart_button.draw()

        exit_button = Button(WHITE, (game_over_word.get_width(
        ) * 0.7, 40), (restart_button.background_rect.x, restart_button.background_rect.y + 60), 30, "Exit", BLACK)
        exit_button.draw()

        pygame.display.update()

    @classmethod
    def restart(cls):
        cls.score = 0
        cls.point_time_count = 0
