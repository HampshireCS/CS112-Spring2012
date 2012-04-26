import pygame
from pygame import Rect, Surface

from layer import Layer

class ShadowLayer(Layer):

    color = 0,0,0,150
    ratio = 3.0 / 4.0

    def draw_sprite(self, sprite, ratio=None):
        if ratio is None:
            ratio = self.ratio

        # calculate the size of the shadow
        w = sprite.rect.width * ratio + 1
        h = w/2
        rect = Rect(0,0,w,h)
        
        # shrink the shadow according to height
        if hasattr(sprite, "height"):
            height0 = sprite.__class__.height
            ratio = (height0 - sprite.height) / float(height0)
            rect.width = max(8, rect.width * ratio)
            rect.height = max(4, rect.height * ratio)

        # move the the midbottom of the sprite
        rect.center = sprite.rect.midbottom
        rect.x -= 1
        rect.y -= 3

        # if the sprite has a height property, use it to move the shadow
        if hasattr(sprite, "height"):
            rect.y += sprite.height


        # draw to the layer
        pygame.draw.ellipse(self._layer, self.color, rect)
#        self._layer.fill(self.color, rect)

