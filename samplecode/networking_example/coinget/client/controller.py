from louie import dispatcher
import pygame
from pygame.locals import *

from coinget import signals

class PlayerController(object):
    _watched = [ K_UP, K_LEFT, K_RIGHT, K_DOWN ]
    def __init__(self, player):
        self.player = player
        self._pressed = {}

    def handle_event(self, event):
        if event.type == KEYDOWN:
            self.on_keydown(event)
        elif event.type == KEYUP:
            self.on_keyup(event)

    def on_keydown(self, event):
        if event.key in self._watched:
            self._pressed[event.key] = True
            self.update()

    def on_keyup(self, event):
        if event.key in self._watched:
            self._pressed[event.key] = False
            self.update()

    def update(self):
        if self._pressed.get(K_LEFT) and self._pressed.get(K_RIGHT):
            x = 0
        elif self._pressed.get(K_LEFT):
            x = -1
        elif self._pressed.get(K_RIGHT):
            x = 1
        else:
            x = 0

        if self._pressed.get(K_UP) and self._pressed.get(K_DOWN):
            y = 0
        elif self._pressed.get(K_UP):
            y = -1
        elif self._pressed.get(K_DOWN):
            y = 1
        else:
            y = 0

        dispatcher.send(signal=signals.MOVE_PLAYER, sender=self.player, x=self.player.x, y=self.player.y, vx=x, vy=y)
