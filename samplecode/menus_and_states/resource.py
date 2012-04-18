import os
from os.path import abspath, dirname

import pygame

ROOT_DIR = dirname(abspath(__file__))
DATA_DIR = os.path.join(ROOT_DIR, "data")

SFX_DIR = os.path.join(DATA_DIR, "sfx")
MUSIC_DIR = os.path.join(DATA_DIR, "music")
IMG_DIR = os.path.join(DATA_DIR, "images")


def play_song(song, times=-1):
    path = os.path.join(MUSIC_DIR, song + ".ogg")
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(times)


_images = {}
def load_image(name):
    if name not in _images:
        path = os.path.join(IMG_DIR, name + ".bmp")
        _images[name] = pygame.image.load(path)

    return _images[name].convert()

_sfx = {}
def load_sfx(name):
    if name not in _sfx:
        path = os.path.join(SFX_DIR, name + ".ogg")
        _sfx[name] = pygame.mixer.Sound(path)

    return _sfx[name]
