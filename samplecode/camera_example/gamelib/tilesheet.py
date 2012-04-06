"""
tilesheet.py

"""

from pygame import Surface
from pygame.sprite import Sprite, Group

class Tile(Sprite):
    def __init__(self, typ, image, loc, collides):
        Sprite.__init__(self)
        self.type = typ
        self.image = image
        self.rect = image.get_rect()
        self.rect.topleft = loc
        self.collides = collides
    

class TileSheet(object):
    _map = {
        # name      loc       collides
        "grass":  [ (20, 30), False ],   
        "flower": [ (20, 150), True ],
        "path":   [ (210, 50), False ]
    }

    def __init__(self, image, size):
        self.image = image
        self.w, self.h = size

        self.tilemap = {}
        for name, data in self._map.items():
            x,y = data[0]
            
            tile = {}
            tile["image"] = image.subsurface(x, y, self.w, self.h)
            tile["collides"] = data[1]
            self.tilemap[name] = tile


    def build(self, data):
        rows = len(data)
        cols = len(data[0])

        tiles = Group()
        for y, row in enumerate(data):
            for x, cell in enumerate(row):
                data = self.tilemap.get(cell)
                if data:
                    tile = Tile(cell, data["image"], (x*self.w, y*self.h), data["collides"])
                    tiles.add(tile)

        return tiles, (cols * self.w, rows * self.h)
