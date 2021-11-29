import pygame
from config import *


class SpriteManager:
    background_sprites = pygame.sprite.LayeredUpdates()
    spawner_timer = 0
    level = 1
    level_timer = 0
    scroll_speed = 5 * level

    @classmethod
    def background_scroll(cls):
        for sprite in cls.background_sprites:
            sprite.rect.x -= cls.scroll_speed

    @classmethod
    def spawn(cls):
        cls.spawner_timer += 1
        # TODO: Increase frequency base on level
        if cls.spawner_timer == 60 * 3:
            pygame.event.post(pygame.event.Event(SPAWN))
            cls.spawner_timer = 0

    @classmethod
    def sprite_recycle(cls):
        for sprite in cls.background_sprites:
            if not sprite.rect.width == WIN_WIDTH * 2 and sprite.rect.x < -100:
                sprite.kill()

    @classmethod
    def level_countdown(cls):
        cls.level_timer += 1
        cls.level = cls.level_timer // (60 * 20)
        cls.scroll_speed = 5 + cls.level * 3
