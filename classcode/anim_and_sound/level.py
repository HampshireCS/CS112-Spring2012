"""
level.py

"""

import os

import pygame
from pygame import Rect, Surface
from pygame.sprite import Group, spritecollide

from player import Player
from coin import CoinGroup

class Level(object):
    initial_coins = 20

    def __init__(self, size):
        self.bounds = Rect((0,0), size)

    def draw(self, surf):
        self.draw_background(surf)
        self.coins.draw(surf)
        surf.blit(self.player.image, self.player.rect)

    def draw_background(self, surf):
        surf.fill((80, 80, 80))

    def restart(self):
        self.player = Player()
        self.player.rect.center = self.bounds.center

        self.coins = CoinGroup(self.bounds)

        # create initial coins
        for i in range(self.initial_coins):
            self.coins.spawn()
    
    def update(self, dt):
        self.player.update(dt)
        self.coins.update(dt)

        # lock player in bounds
        self.player.rect.clamp_ip(self.bounds)

        spritecollide(self.player, self.coins, True)

