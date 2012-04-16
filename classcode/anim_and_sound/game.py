"""
game.py

"""

import pygame
from pygame.locals import *
from pygame.sprite import spritecollide, GroupSingle

from level import Level

class Game(object):
    fps = 60

    def __init__(self, screen):
        self.screen = screen
        self.level = Level(self.screen.get_size())

    def quit(self):
        self.done = True


    def update(self):
        dt = self.clock.tick(self.fps)
        self.level.update(dt)

    def draw(self):
        self.level.draw(self.screen)


    def run(self):
        self.done = False
        self.clock = pygame.time.Clock()
        self.level.restart()

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

