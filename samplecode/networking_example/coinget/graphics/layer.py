import pygame
from pygame import Surface


class Layer(object):

    def __init__(self, size):
        self._layer = Surface(size, pygame.SRCALPHA)

    def clear(self):
        self._layer.fill((0,0,0,0))

    def draw_sprites(self, sprites):
        for sprite in sprites:
            self.draw_sprite(sprite)

    def draw_sprite(self, sprite):
        self._layer.blit(sprite.image, sprite.rect)

    def draw(self, surf, loc=(0,0)):
        surf.blit(self._layer, loc)
