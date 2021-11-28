import pygame
import random
from pygame.sprite import Group, GroupSingle
from config import *
from background import Background
from fish import NormalFish, PoisonedFish
from shark import Shark
from trash import Trash
from sprites import SpriteManager
from UI import UI


def collision(shark_group: GroupSingle,
              trash_group: Group,
              normal_fish_group: Group,
              poisoned_fish_group: Group) -> list:
    shark_trash_collision_list = pygame.sprite.spritecollide(
        shark_group.sprite, trash_group, True)
    shark_normal_collision_list = pygame.sprite.spritecollide(
        shark_group.sprite, normal_fish_group, True)
    shark_poisoned_collision_list = pygame.sprite.spritecollide(
        shark_group.sprite, poisoned_fish_group, True)

    if shark_trash_collision_list:
        # be invincible for a while
        shark_group.sprite.collision("trash")
    if shark_normal_collision_list:
        UI.score += 10
        shark_group.sprite.collision("normal")
    if shark_poisoned_collision_list:
        UI.score += 20
        shark_group.sprite.collision("poisoned")


def render(background_manager: SpriteManager,
           background_group: GroupSingle,
           shark_group: GroupSingle,
           trash_group: Group,
           normal_fish_group: Group,
           poisoned_fish_group: Group):

    background_manager.background_scroll()

    background_group.update()
    background_group.draw(WINDOW_SURFACE)

    trash_group.draw(WINDOW_SURFACE)

    normal_fish_group.draw(WINDOW_SURFACE)
    poisoned_fish_group.draw(WINDOW_SURFACE)

    shark_group.update()
    shark_group.draw(WINDOW_SURFACE)

    UI.display_health_poison_bar(shark_group.sprite)
    UI.display_score()

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

    trash_group = pygame.sprite.Group()
    normal_fish_group = pygame.sprite.Group()
    poisoned_fish_group = pygame.sprite.Group()

    # TODO: Friquency will increase while time pass
    pygame.time.set_timer(SPAWN, 3000)

    game_over = False
    is_running = True
    while is_running:
        clock.tick(60)
        UI.point_timer()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.KEYDOWN:
                pressed_key = pygame.key.get_pressed()
                shark.movement(pressed_key)
            if event.type == SPAWN:
                choice = random.choice(["trash", "normal", "poisoned"])
                if choice == "trash":
                    trash = Trash()
                    trash_group.add(trash)
                    sprite_manager.background_sprites.add(trash)
                elif choice == "normal":
                    normal_fish = NormalFish()
                    normal_fish_group.add(normal_fish)
                    sprite_manager.background_sprites.add(normal_fish)
                elif choice == "poisoned":
                    poisoned_fish = PoisonedFish()
                    normal_fish_group.add(poisoned_fish)
                    sprite_manager.background_sprites.add(poisoned_fish)
            if event.type == GAME_OVER:
                game_over = True

        if not game_over:
            collision(shark_group, trash_group,
                      normal_fish_group, poisoned_fish_group)
            render(sprite_manager, background_group, shark_group,
                   trash_group, normal_fish_group, poisoned_fish_group)
        else:
            UI.game_over()

    pygame.quit()


if __name__ == "__main__":
    main()
