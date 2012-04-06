"""
level.py

"""

import os

from pygame import Rect, Surface
from pygame.sprite import Group

from settings import DATA_DIR

class Level(object):

    _map = {
        "%": "flower",
        "~": "grass",
        ".": "path"
    }

    def __init__(self, name, tilesheet):
        # load level data
        path = os.path.join(DATA_DIR, "levels", name) + ".lvl"
        with open(path, "r") as f:
            data = f.read().strip().split("\n")

        # parse level data
        data = [ [ self._map.get(c) for c in row ] for row in data ]

        # build the level
        self.tiles, size = tilesheet.build(data)
        self.bounds = Rect((0,0), size)

        # find path
        self.path = Group()
        for tile in self.tiles:
            if tile.type == "path":
                self.path.add(tile)

        # render
        self.render_background()

        

    def render_background(self):
        self.background = Surface(self.bounds.size)
        self.tiles.draw(self.background)        



