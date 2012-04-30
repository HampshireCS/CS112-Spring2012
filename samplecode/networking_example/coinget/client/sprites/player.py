from louie import dispatcher

import pygame
from pygame.sprite import Sprite, Group

from coinget import signals
from coinget.world import Player


class PlayerSprite(Sprite):
    def __init__(self, player):
        Sprite.__init__(self)

        self.image = pygame.Surface(player.rect.size)
        self.rect = self.image.get_rect()

        self.image.fill((0,0,0))
        self.image.fill(player.color, self.rect.inflate(-4,-4))

        self.rect.center = player.rect.center

        self.player = player
        print "local", self.player.local
        dispatcher.connect(self.kill, signal=signals.DEL_OBJECT, sender=player)

    def update(self):
        self.rect.center = self.player.rect.center


class PlayerGroup(Group):
    def __init__(self):
        Group.__init__(self)

        dispatcher.connect(self.add_sprite, signal=signals.NEW_OBJECT, sender=Player)

    def add_sprite(self, obj):
        self.add(PlayerSprite(obj))
