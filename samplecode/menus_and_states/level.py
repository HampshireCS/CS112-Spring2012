"""
level.py

"""

import os

import pygame
from pygame import Rect, Surface
from pygame.sprite import Group, spritecollide

from resource import load_image, play_song, load_sfx

from player import Player
from coin import CoinGroup

class Level(object):
    initial_coins = 20
    song = "maintheme"

    def __init__(self, size):
        self.bounds = Rect((0,0), size)
        self.bg_tile = load_image("grass")
        self.coin_sfx = load_sfx("coin")

    def draw_background(self, surf):
        tw, th = self.bg_tile.get_size()
        sw, sh = surf.get_size()

        for y in range(0, sh, th):
            for x in range(0, sw, tw):
                surf.blit(self.bg_tile, (x,y))

    def restart(self):
        self.player = Player()
        self.player.rect.center = self.bounds.center

        self.coins = CoinGroup(self.bounds)

        # create initial coins
        for i in range(self.initial_coins):
            self.coins.spawn()

        # start the background music
        play_song(self.song)  
    
    def update(self, dt):
        self.player.update(dt)
        self.coins.update(dt)

        # lock player in bounds
        self.player.rect.clamp_ip(self.bounds)

        # collide player with coins
        if spritecollide(self.player, self.coins, True):
            self.coin_sfx.stop()
            self.coin_sfx.play()

    def draw(self, surf):
        self.draw_background(surf)
        self.coins.draw(surf)
        surf.blit(self.player.image, self.player.rect)
