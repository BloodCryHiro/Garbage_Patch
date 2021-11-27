import pygame
from pygame.sprite import Group, GroupSingle
from config import *
from background import Background
from sprites import SpriteManager


def render(background_group: GroupSingle):
    background_group.draw(WINDOW_SURFACE)

    pygame.display.update()


def main():
    pygame.init()
    pygame.display.set_caption("Garbage Patch")

    sprite_manager = SpriteManager()

    background = Background()
    background_group = pygame.sprite.GroupSingle()
    background_group.add(background)
    sprite_manager.background_sprites.add(background)

    isRunning = True
    while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False

        render(background_group)

    pygame.quit()


if __name__ == "__main__":
    main()
