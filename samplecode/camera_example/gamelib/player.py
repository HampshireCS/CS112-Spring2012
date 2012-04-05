"""
player.py

"""

from pygame import Surface
from pygame.sprite import Sprite

class Player(Sprite):

    def __init__(self, level):
        Sprite.__init__(self)

        self.level = level

        self.image = Surface((120, 80))
        self.image.fill((0,150,0))
        self.rect = self.image.get_rect()

        self.x, self.y = level.bounds.center
        self.vy = 5

    def update(self, dt):
        self.y += self.vy

        if self.y < self.level.bounds.top or self.y > self.level.bounds.bottom:
            self.vy = -self.vy
            self.y += 2 * self.vy


        # update player 
        self.rect.center = int(self.x), int(self.y)
