"""
level.py

"""

import os

from pygame import Rect, Surface
from pygame.sprite import Sprite, Group

from settings import LEVEL_SIZE

class Block(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = Surface((w,h))
        self.image.fill(0)
        self.rect = Rect(x,y,w,h)

class Level(object):

    def __init__(self):
        self.bounds = Rect((0,0), LEVEL_SIZE)

        # make rects for level
        self.blocks = Group(
            Block(0,0,40,self.bounds.height),                   # left wall
            Block(self.bounds.width - 40, 0, 40, self.bounds.height),  # right wall
            Block(0, self.bounds.height - 40, self.bounds.width, 40),         # floor
            Block(self.bounds.centerx + 60, self.bounds.height - 120, 40, 120), # random thing
            Block(0, self.bounds.height - 50, 80, 50),
            Block(self.bounds.centerx + 160, self.bounds.height - 140, self.bounds.width, 40)
        )


        # render
        self.render_background()

    def render_background(self):
        self.background = Surface(self.bounds.size)
        self.background.fill((80,80,80))
        self.blocks.draw(self.background)



