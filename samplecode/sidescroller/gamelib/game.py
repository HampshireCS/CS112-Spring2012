"""
game.py

"""

import pygame
from pygame.locals import *
from pygame.sprite import spritecollide

from camera import Camera
from level import Level
from player import Player

from settings import FPS


class Game(object):

    def __init__(self, screen):
        self.screen = screen

        self.level = Level()
        self.player = Player(self.level)

        self.hud = screen.subsurface((0, 0, screen.get_width(), 40))
        self.game_area = screen.subsurface((0, 40, screen.get_width(), screen.get_height() - 40))

        self.cam = Camera(self.player, self.level.bounds, self.game_area.get_size())

        self.font = pygame.font.Font(None, 36)

        self.score = 0


    def quit(self):
        self.done = True

    def update(self):
        dt = self.clock.tick(FPS)

        self.player.update(dt)
        self.cam.update(self.player.rect)


    def draw(self):
        # draw level
        self.cam.draw_background(self.game_area, self.level.background)
        self.cam.draw_sprite(self.game_area, self.player)

        # draw hud
        self.hud.fill((20,20,20))
        text = self.font.render("Score: %04d" % self.score, True, (255,255,255), (20, 20, 20))
        self.hud.blit(text, (15, 10))

    def run(self):
        self.done = False
        self.clock = pygame.time.Clock()

        while not self.done:
            # input
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.quit()
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    self.quit()
                elif event.type == KEYDOWN and event.key == K_SPACE:
                    self.player.jump()

            self.update()
            self.draw()
            pygame.display.flip()

