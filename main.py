import pygame
from pygame.sprite import Group, GroupSingle
from config import *
from background import Background
from shark import Shark
from sprites import SpriteManager


def update(background_manager: SpriteManager):
    background_manager.background_scroll()


def render(background_group: GroupSingle, shark_group: GroupSingle):
    background_group.update()
    background_group.draw(WINDOW_SURFACE)

    shark_group.draw(WINDOW_SURFACE)

    pygame.display.update()


def main():
    pygame.init()
    pygame.display.set_caption("Garbage Patch")
    clock = pygame.time.Clock()

    sprite_manager = SpriteManager()

    background = Background()
    background_group = pygame.sprite.GroupSingle()
    background_group.add(background)
    sprite_manager.background_sprites.add(background)

    shark = Shark()
    shark_group = pygame.sprite.GroupSingle()
    shark_group.add(shark)

    isRunning = True
    while isRunning:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
            if event.type == pygame.KEYDOWN:
                pressed_key = pygame.key.get_pressed()
                shark.movement(pressed_key)

        update(sprite_manager)
        render(background_group, shark_group)

    pygame.quit()


if __name__ == "__main__":
    main()
