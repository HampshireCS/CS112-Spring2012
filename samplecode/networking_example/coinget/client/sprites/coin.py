from louie import dispatcher

import pygame
from pygame.sprite import Sprite, Group

from coinget import signals
from coinget.world import Coin


class CoinSprite(Sprite):
    def __init__(self, coin):
        Sprite.__init__(self)

        self.image = pygame.Surface(coin.rect.size)
        self.rect = self.image.get_rect()

        self.image.fill((0,0,0))
        self.image.fill((255,255,0), self.rect.inflate(-4,-4))

        self.rect.center = coin.rect.center

        self.coin = coin
        dispatcher.connect(self.kill, signal=signals.DEL_OBJECT, sender=coin)


class CoinGroup(Group):
    def __init__(self):
        Group.__init__(self)

        dispatcher.connect(self.add_sprite, signal=signals.NEW_OBJECT, sender=Coin)

    def add_sprite(self, obj):
        self.add(CoinSprite(obj))
