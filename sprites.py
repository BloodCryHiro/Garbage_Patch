import pygame


class SpriteManager:
    def __init__(self):
        self.background_sprites = pygame.sprite.LayeredUpdates()

    def background_scroll(self):
        # TODO: Increase by time pass
        scroll_speed = 5
        for sprite in self.background_sprites:
            sprite.rect.x -= scroll_speed
