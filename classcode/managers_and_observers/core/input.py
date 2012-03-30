import pygame
from pygame.locals import *

class KeyListener(object):
    def on_keydown(self, event): pass
    def on_keyup(self, event): pass


class MouseListener(object):
    def on_buttondown(self, event): pass
    def on_buttonup(self, event): pass
    def on_motion(self, event): pass

class InputManager(object):
    def __init__(self):
        self._key = []
        self._mouse = []

    def add_mouse_listener(self, listener):
        self._mouse.append(listener)

    def add_key_listener(self, listener):
        self._key.append(listener)

    def handle_event(self, event):
        if event.type == KEYDOWN:
            for listener in self._key:
                listener.on_keydown(event)
        elif event.type == KEYUP:
            for listener in self._key:
                listener.on_keyup(event)

        elif event.type == MOUSEBUTTONDOWN:
            for listener in self._mouse:
                listener.on_buttondown(event)
        elif event.type == MOUSEBUTTONUP:
            for listener in self._mouse:
                listener.on_buttonup(event)
        elif event.type == MOUSEMOTION:
            for listener in self._mouse:
                listener.on_motion(event)
