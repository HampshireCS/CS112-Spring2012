from random import randrange

from louie import dispatcher
from pygame import Rect

from coinget import settings
from coinget import signals
from obj import WorldObject


## Coin
class Coin(WorldObject):
    life = settings.COIN_LIFE

    def __init__(self, identifier, loc):
        WorldObject.__init__(self, identifier)

        self.rect = Rect((0,0), settings.COIN_SIZE)
        self.rect.center = loc

    def update(self, dt):
        self.life -= dt

        if self.life <= 0:
            self.kill()

    def __repr__(self):
        return "<Coin: (%d, %d) %f>" % (self.rect.centerx, self.rect.centery, self.life)
