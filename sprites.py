import pygame
from config import *


class SpriteManager:
    background_sprites = pygame.sprite.LayeredUpdates()
    scroll_speed = 5

    @classmethod
    def background_scroll(cls):
        # TODO: Increase by time pass
        for sprite in cls.background_sprites:
            sprite.rect.x -= cls.scroll_speed

    @classmethod
    def sprite_recycle(cls):
        for sprite in cls.background_sprites:
            if not sprite.rect.width == WIN_WIDTH * 2 and sprite.rect.x < -100:
                sprite.kill()
