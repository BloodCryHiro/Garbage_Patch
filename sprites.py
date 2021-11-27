import pygame


class SpriteManager:
    def __init__(self):
        self.background_sprites = pygame.sprite.LayeredUpdates()
