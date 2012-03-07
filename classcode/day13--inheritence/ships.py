#!/usr/bin/env python

from random import randrange

import pygame
from pygame import Rect, Surface
from pygame.locals import *
from pygame.sprite import Sprite, Group

class Ship(Sprite):
    width = 20
    height = 20

    def __init__(self, x, y, vx, vy, bounds, color):
        Sprite.__init__(self)

        self.vx = vx
        self.vy = vy
        self.bounds = bounds
        self.color = color

        self.rect = Rect(x, y, self.width, self.height)
        self.image = Surface(self.rect.size)
        self.draw_image()
        
    def draw_image(self):
        self.image.fill(self.color)

    def update(self, dt):
        dt /= 1000.0
        dx = int(self.vx * dt)
        dy = int(self.vy * dt)
        self.rect.x += dx
        self.rect.y += dy

        if self.rect.left < self.bounds.left or self.rect.right > self.bounds.right:
            self.vx = -self.vx
            self.rect.x += -2 * dx

        if self.rect.top < self.bounds.top or self.rect.bottom > self.bounds.bottom:
            self.vy = -self.vy
            self.rect.y += -2 * dy



class ShipSpawner(object):
    ship_type = Ship

    def __init__(self, duration, group, bounds):
        self.group = group
        self.bounds = bounds
        self.duration = duration
        self.time = duration

    def rand_vel(self):
        return 100, 100

    def rand_color(self):
        return 255, 255, 0

    def spawn(self):
        x = randrange(self.bounds.width - self.ship_type.width) + self.bounds.left
        y = randrange(self.bounds.height - self.ship_type.height) + self.bounds.top
        vx, vy = self.rand_vel()
        color = self.rand_color()

        ship = self.ship_type(x, y, vx, vy, self.bounds, color)
        self.group.add(ship)

    def update(self, dt):
        self.time += dt
        if self.time >= self.duration:
            self.time = 0
            self.spawn()


