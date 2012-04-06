"""
player.py

"""
import pygame
from pygame.locals import *
from pygame import Surface
from pygame.sprite import Sprite

from settings import PLAYER_COLOR, PLAYER_SPEED

class Player(Sprite):

    def __init__(self, bounds):
        Sprite.__init__(self)

        self.bounds = bounds

        self.image = Surface((80, 80))
        self.rect = self.image.get_rect()

        self.image.fill((0,0,0))
        self.image.fill(PLAYER_COLOR, self.rect.inflate(-4,-4))

        self.x, self.y = bounds.center
        self.vx = PLAYER_SPEED
        self.vy = PLAYER_SPEED

    def update(self, dt):
        dt = dt / 1000.0
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            self.y -= self.vy * dt
        if keys[K_DOWN]:
            self.y += self.vy * dt
        if keys[K_LEFT]:
            self.x -= self.vx * dt
        if keys[K_RIGHT]:
            self.x += self.vx * dt

        # update player 
        self.rect = self.image.get_rect()
        self.rect.center = int(self.x), int(self.y)
        self.rect.clamp_ip(self.bounds)
