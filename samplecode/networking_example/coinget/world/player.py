import math

from louie import dispatcher
from pygame import Rect

from coinget import settings
from coinget import signals

from obj import WorldObject


class Player(WorldObject):
    def __init__(self, identifier, nick, color, pos, vel=(0,0)):
        WorldObject.__init__(self, identifier)

        self.nick = nick
        self.color = color
        self.rect = Rect((0,0), settings.PLAYER_SIZE)
        self.vx, self.vy = vel
        self.x, self.y = pos
        self.rect.center = pos
        self.local = False

        dispatcher.connect(self.move, signal=signals.MOVE_PLAYER, sender=self)


    def move(self, x, y, vx, vy):
        if vx and vy:
            vx *= 1 / math.sqrt(2)
            vy *= 1 / math.sqrt(2)

        self.x = x
        self.y = y
        self.vx = vx * settings.PLAYER_SPEED
        self.vy = vy * settings.PLAYER_SPEED


    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

        self.rect.centerx = self.x
        self.rect.centery = self.y

        clamp = self.rect.clamp(self.world.bounds)
        if clamp != self.rect:
            self.rect = clamp
            self.x = self.rect.centerx
            self.y = self.rect.centery

