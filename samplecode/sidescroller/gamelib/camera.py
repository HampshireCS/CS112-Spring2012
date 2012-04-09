"""
camera.py

"""

from pygame import Rect

from util import rel_rect

class Camera(object):

    def __init__(self, target, bounds, size):
        self.bounds = bounds
        self.rect = Rect((0,0), size)

    def update(self, target):
        self.rect.center = target.center
        self.rect.clamp_ip(self.bounds)

    def draw_background(self, surf, bg):
        surf.blit(bg, (-self.rect.x, -self.rect.y))

    def draw_sprite(self, surf, sprite):
        if self.rect.colliderect(sprite.rect):
            surf.blit(sprite.image, rel_rect(sprite.rect, self.rect))
