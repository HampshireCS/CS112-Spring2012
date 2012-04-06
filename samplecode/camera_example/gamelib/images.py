"""
images.py

Handles images don'tcha know
"""

import os

import pygame

from settings import DATA_DIR

class ImageManager(object):
    _instance = None

    # image manager is a singleton
    def __new__(cls, *a, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *a, **kw)
        return cls._instance

    def __init__(self):
        self._images = {}

    def load(self, name, colorkey=None):
        if name not in self._images:
            path = os.path.join(DATA_DIR, "images", name) + ".bmp"
            image = pygame.image.load(path).convert()
            if colorkey:
                if colorkey == -1:
                    colorkey = image.get_at((0,0))
                image.set_colorkey(colorkey)

            self._images[name] = image

        return self._images[name].convert()
