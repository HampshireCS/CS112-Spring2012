"""
player.py

"""
import pygame
from pygame.locals import *
from pygame import Surface
from pygame.sprite import Sprite, Group

from settings import PLAYER_COLOR, PLAYER_SPEED, PLAYER_SIZE, PLAYER_JUMP_SPEED, GRAVITY

class Player(Sprite):

    def __init__(self, level):
        Sprite.__init__(self)

        self.level = level
        self.bounds = level.bounds

        self.image = Surface(PLAYER_SIZE)
        self.rect = self.image.get_rect()

        self.image.fill((0,0,0))
        rect = self.image.get_rect().inflate(-4, -4)
        self.image.fill((255,0,0), rect)

        self.rect = self.image.get_rect()
        self.rect.center = self.bounds.center

        self.vx = 0
        self.vy = 0
        self.inair = True

    def jump(self):
        if not self.inair:
            self.inair = True
            self.vy = PLAYER_JUMP_SPEED
    
    def touches(self, group):
        touching = Group()
        coll = self.rect.inflate(1,1) # grow 1px to allow for edges
        for sprite in group:
            if coll.colliderect(sprite.rect):
                touching.add(sprite)
        return touching

    def update(self, dt):
        dt = dt / 1000.0
        keys = pygame.key.get_pressed()

        self.vx = 0
        if keys[K_LEFT]:
            self.vx -= PLAYER_SPEED
        if keys[K_RIGHT]:
            self.vx += PLAYER_SPEED

        self.vy -= dt * GRAVITY
        dx = self.vx * dt
        dy = -self.vy * dt

        # update position
        prev_rect = self.rect
        self.rect = self.rect.move(dx, dy)
        self.rect.clamp_ip(self.bounds)   # temp error

        self.inair = True
        for sprite in self.touches(self.level.blocks):
            rect = sprite.rect 

            # collide with walls
            if self.rect.left <= rect.right and prev_rect.left >= rect.right:
                self.rect.left = rect.right
            if self.rect.right >= rect.left and prev_rect.right <= rect.left:
                self.rect.right = rect.left

            # handle cielings
            if self.rect.top <= rect.bottom and prev_rect.top >= rect.bottom:
                self.vy /= 2.0   # halve speed from hitting head
                self.rect.top = rect.bottom

            # handle landing
            if self.rect.bottom >= rect.top and prev_rect.bottom <= rect.top:
                self.vy = 0
                self.rect.bottom = rect.top
                self.inair = False
    
