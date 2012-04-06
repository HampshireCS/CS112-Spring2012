"""
player.py

Player class for our shmup
"""
import pygame
from pygame import Surface
from pygame.sprite import Sprite, Group


class Player(Sprite):
    color = 255, 255, 0
    size = 20, 20
    
    def __init__(self, loc, bounds):
        Sprite.__init__(self)

        self.image = Surface(self.size)
        self.rect = self.image.get_rect()

        self.rect.center = loc
        self.bounds = bounds

        self.image.fill(self.color)
        self.bullets = Group()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        self.rect.clamp_ip(self.bounds)

    def shoot(self):
        if not self.alive():
            return

        bullet = Bullet(self.bounds)
        bullet.rect.midbottom = self.rect.midtop
        self.bullets.add(bullet)


class Bullet(Sprite):
    size = 5, 10
    color = 0, 255, 0
    speed = 12

    def __init__(self, bounds):
        Sprite.__init__(self)

        self.image = Surface(self.size)
        self.rect = self.image.get_rect()
        self.bounds = bounds

        self.image.fill(self.color)

    def update(self):
        self.rect.y -= self.speed
        
        if self.rect.bottom < self.bounds.top:
            self.kill()
