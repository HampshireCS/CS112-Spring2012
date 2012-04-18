from random import randrange

from pygame import Surface
from pygame.sprite import Sprite, Group

from anim import Animation
from spritesheet import SpriteSheet



class CoinAnimation(Animation):
    def __init__(self, duration):
        spritesheet = SpriteSheet("coin", (8, 1))

        frames = [ (duration, (0, 0)),
                   (duration, (1, 0)),
                   (duration, (2, 0)),
                   (duration, (3, 0)),
                   (duration, (4, 0)),
                   (duration, (5, 0)),
                   (duration, (6, 0)),
                   (duration, (7, 0)) ]

        Animation.__init__(self, spritesheet, frames)


## Coin
class Coin(Sprite):
    def __init__(self, loc):
        Sprite.__init__(self)

        self.anim = CoinAnimation(240)
        self.image = self.anim.get_current_frame()
        self.rect = self.image.get_rect()
        self.rect.center = loc


    def update(self, dt):
        self.anim.update(dt)
        self.image = self.anim.get_current_frame()

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

