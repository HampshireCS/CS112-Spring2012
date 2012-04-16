"""
player.py

"""
import math

import pygame
from pygame.locals import *
from pygame import Surface
from pygame.sprite import Sprite

DIAG = 1 / math.sqrt(2)

class Player(Sprite):
    speed = 300

    def __init__(self):
        Sprite.__init__(self)
        self.vx = 0
        self.vy = 0

        self.image = self.create_image()
        self.rect = self.image.get_rect()

    # create image is for temporary artwork
    def create_image(self):
        image = Surface((40, 40))
        rect = image.get_rect()
        image.fill((0,0,0), rect)
        image.fill((255,0,0), rect.inflate(-4,-4))
        return image


    def update(self, dt):
        self.vx, self.vy = 0, 0
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            self.vy = -self.speed
        if keys[K_DOWN]:
            self.vy =  self.speed
        if keys[K_LEFT]:
            self.vx = -self.speed
        if keys[K_RIGHT]:
            self.vx =  self.speed

        if self.vx and self.vy:
            self.vx *= DIAG
            self.vy *= DIAG

        dt = dt / 1000.0
        self.rect.x += self.vx * dt
        self.rect.y += self.vy * dt
