from random import randrange

from pygame import Surface
from pygame.sprite import Sprite, Group


## Coin
class Coin(Sprite):
    def __init__(self, loc):
        Sprite.__init__(self)

        self.image = self.create_image()
        self.rect = self.image.get_rect()
        self.rect.center = loc

    def create_image(self):
        image = Surface((15, 15))
        rect = image.get_rect()
        image.fill((0,0,0), rect)
        image.fill((255,255,0), rect.inflate(-2,-2))
        return image

    def update(self, dt):
        pass

class CoinGroup(Group):
    spawn_rate = 1000   # ms

    def __init__(self, bounds):
        Group.__init__(self)

        self.bounds = bounds
        self.spawn_timer = 0

    def spawn(self):
        x = randrange(self.bounds.x, self.bounds.x + self.bounds.width)
        y = randrange(self.bounds.y, self.bounds.y + self.bounds.height)

        coin = Coin((x,y))
        coin.rect.clamp_ip(self.bounds)
        self.add(coin)

    def update(self, dt):
        Group.update(self, dt)
    
        # update the spawner
        self.spawn_timer += dt
        if self.spawn_timer >= self.spawn_rate:
            self.spawn()
            self.spawn_timer = 0

