"""
camera.py

"""

from pygame import Rect

from util import rel_rect

class Camera(object):

    def __init__(self, player, level, size):
        self.player = player
        self.level = level

        self.rect = Rect((0,0), size)

    def update(self):
        self.rect.center = self.player.rect.center
        self.rect.clamp_ip(self.level.bounds)


    def draw_level(self, surf):
        surf.blit(self.level.background, (-self.rect.x, -self.rect.y))


    def draw_player(self, surf):
        self.draw_sprite(surf, self.player)


    def draw_sprite(self, surf, sprite):
        surf.blit(sprite.image, rel_rect(sprite.rect, self.rect))
