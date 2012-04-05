"""
game.py

"""

import pygame
from pygame.locals import *

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

        self.cam = Camera(self.player, self.level, self.game_area.get_size())

        self.font = pygame.font.Font(None, 36)


    def quit(self):
        self.done = True


    def update(self):
        dt = self.clock.tick(FPS)
        self.player.update(dt)
        self.cam.update()


    def draw(self):
        # draw level
        self.cam.draw_level(self.game_area)
        self.cam.draw_player(self.game_area)

        # draw hud
        self.hud.fill((20,20,20))
        text = self.font.render("This is a HUD", True, (255,255,255), (20, 20, 20))
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

            self.update()
            self.draw()
            pygame.display.flip()

