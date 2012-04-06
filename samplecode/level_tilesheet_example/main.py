#!/usr/bin/env python
import os

import pygame
from pygame.locals import *

## Loading resources
def load_image(name, colorkey=None):
    path = os.path.join("data", "images", name) + ".bmp"

    image = pygame.image.load(path).convert()
    if colorkey:
        image.set_colorkey(colorkey)
    return image


## Tilesheet class
class TileSheet(object):
    _map = {
        "~": (20,30),   # grass
        "%": (20,150),  # flower
        ".": (210,50)   # path
    }

    def __init__(self, image, size):
        self.image = image
        self.w,self.h = size

        # rebuild map
        self.tilemap = {}
        for tile,coord in self._map.items():
            if coord:
                x,y = coord
                self.tilemap[tile] = image.subsurface(x, y, self.w, self.h)

    def render(self, data):
        # create level image
        rows = len(data)
        cols = len(data[0])
        surf = pygame.Surface((cols * self.w, rows * self.h))
        
        # render each tile in it
        for y, row in enumerate(data):
            for x, cell in enumerate(row):
                tile = self.tilemap.get(cell)
                if tile:
                    surf.blit(tile, (x*self.w, y*self.h))

        return surf
        
# Level class
class Level(object):
    def __init__(self, name, tilesheet):
        path = os.path.join("data", "levels", name) + ".lvl"
        f = open(path, "r")
        data = f.read().replace("\r", "").strip().split("\n")
        f.close()

        self.image = tilesheet.render(data)


## Main Game
def main():
    # init pygame
    pygame.init()
    screen = pygame.display.set_mode((400,400))
    pygame.key.set_repeat(50,50)

    # init game
    img_tiles = load_image("tiles", (0,255,200))
    tilesheet = TileSheet(img_tiles, (32, 32))
    level = Level("test_level", tilesheet)
    off_x, off_y = 0, 0

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

            # move the camera
            elif event.type == KEYDOWN and event.key == K_LEFT:
                off_x += 5
            elif event.type == KEYDOWN and event.key == K_RIGHT:
                off_x -= 5
            elif event.type == KEYDOWN and event.key == K_UP:
                off_y += 5
            elif event.type == KEYDOWN and event.key == K_DOWN:
                off_y -= 5

        # update

        # draw
        screen.fill((80,80,80))
        screen.blit(level.image, (off_x, off_y))

        # tick
        pygame.display.flip()
        clock.tick(30)
# main
if __name__ == "__main__":
    main()
    print "ByeBye"

