#!/usr/bin/env python
from random import randrange

import pygame
from pygame.locals import *
from pygame.sprite import Group, GroupSingle, groupcollide

from enemy import Enemy, FastEnemy
from player import Player

SCREEN_SIZE = 480,640
BG_COLOR = 0,0,0

def main():
    # initialze pygame
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    bounds = screen.get_rect()

    # initialize the game
    player = Player(bounds.center, bounds)
    player_grp = GroupSingle(player)
    enemies = Group()
    spawn_counter = 0
    fast_spawn_counter = 0
    score = 0

    font = pygame.font.Font(None, 40)

    # game loop
    done = False
    clock = pygame.time.Clock()
    while not done:
        # input
        for event in pygame.event.get():
            if event.type == QUIT:
                done = True
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                done = True
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                player.shoot()
            elif event.type == KEYDOWN and event.key == K_SPACE and not player.alive():
                player = Player(bounds.center, bounds)
                player_grp.add(player)
                score = 0
                for enemy in enemies:
                    enemy.kill()
                # same as enemies.empty()

        # update
        player_grp.update()
        player.bullets.update()
        enemies.update()

        # spawn enemies
        spawn_counter += 1
        if spawn_counter >= 10:
            n = randrange(4)
            for i in range(n):
                x = randrange(bounds.width - Enemy.width) 
                enemy = Enemy((x, 0), bounds)
                enemies.add(enemy)
            spawn_counter = 0

        # fast spawn 
        fast_spawn_counter += 1
        if fast_spawn_counter >= 45:
            x = randrange(bounds.width - FastEnemy.width)
            enemy = FastEnemy((x, 0), bounds)
            enemies.add(enemy)
            fast_spawn_counter = 0

        # collisions
        groupcollide(player_grp, enemies, True, False)

        for enemy in groupcollide(enemies, player.bullets, True, True):
            if player.alive():
                score += 1

        # draw
        screen.fill(BG_COLOR)
        player_grp.draw(screen)
        player.bullets.draw(screen)
        enemies.draw(screen)

        score_text = font.render("Score: %08d"%score, False, (255, 255, 255))
        screen.blit(score_text, (5, 5))

        if not player.alive():
            gameover = font.render("Press Space to Respawn", False, (255, 255, 255))
            rect = gameover.get_rect()
            rect.center = screen.get_rect().center
            screen.blit(gameover, rect)

        pygame.display.flip()

        clock.tick(30)


# when this program is run, call "main()"
if __name__ == "__main__":
    main()
    print "ByeBye"
