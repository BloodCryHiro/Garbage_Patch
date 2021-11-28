import pygame


class Shark(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(
            pygame.image.load("Assets/Arts/shark.png"), (100, 50))
        self.rect = self.image.get_rect(center=(100, 350))

    def movement(self, pressed_key):
        if pressed_key[pygame.K_UP] and not self.rect.center == (100, 200):
            self.rect.y -= 150
        elif pressed_key[pygame.K_DOWN] and not self.rect.center == (100, 500):
            self.rect.y += 150
