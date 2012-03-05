#!/usr/bin/env python

import math

from random import randrange

import pygame
from pygame.locals import *


## Settings
C_BLACK = 0,0,0
C_RED = 255,0,0


## from tiefighter.py
def draw_tie(surf, color, size):
    wall = size / 8

    surf.fill(C_BLACK)
    pygame.draw.rect(surf, color, (0, 0, wall, size))
    pygame.draw.rect(surf, color, (size-wall, 0, wall, size))
    pygame.draw.rect(surf, color, (0, (size-wall)/2, size, wall))
    pygame.draw.circle(surf, color, (size/2, size/2), size/4)



class Game(object):
    title = "Tie Hunt"
    size = 800, 600
    fps = 30

    def __init__(self):
        self.screen = pygame.display.set_mode(self.size)
        self.bounds = self.screen.get_rect()
        pygame.display.set_caption(self.title)

    def run(self):
        clock = pygame.time.Clock()
        done = False
        while not done:
            # tick
            clock.tick(self.fps)

            # input
            for event in pygame.event.get():
                if event.type == QUIT:
                    done = True
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    done = True

            # update

            # draw
            self.screen.fill(C_BLACK)
            pygame.display.flip()



if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.run()
    print "Bye Bye"
