#!/usr/bin/env python

import math
from random import randrange

import pygame
from pygame import Rect, Surface
from pygame.locals import *
from pygame.sprite import Sprite, Group

from app import Application
from graphics import draw_tie, draw_ywing
from ships import Ship, ShipSpawner
from utils import *


class Game(Application):
    title = "Spaceships"
    screen_size = 800, 600


if __name__ == "__main__":
    Game().run()
    print "ByeBye"
