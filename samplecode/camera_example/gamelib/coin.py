from random import randrange

from pygame import Surface
from pygame.sprite import Sprite, Group

from settings import COIN_COLOR, COIN_SPAWN_RATE

class Coin(Sprite):

    def __init__(self, loc):
        Sprite.__init__(self)

        self.image = Surface((30, 30))
        self.rect = self.image.get_rect()

        self.image.fill((0,0,0))
        self.image.fill(COIN_COLOR, self.rect.inflate(-2, -2))
        self.rect.center = loc


class CoinGroup(Group):
    def __init__(self, bounds):
        Group.__init__(self)

        self.bounds = bounds

        self.spawn_rate = COIN_SPAWN_RATE * 1000
        self.spawn_timer = 0

    def spawn(self):
        x = randrange(self.bounds.x, self.bounds.x + self.bounds.width)
        y = randrange(self.bounds.y, self.bounds.y + self.bounds.height)

        coin = Coin((x,y))
        coin.rect.clamp_ip(self.bounds)
        self.add(coin)

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer >= self.spawn_rate:
            self.spawn()
            self.spawn_timer = 0


