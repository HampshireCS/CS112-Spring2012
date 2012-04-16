from random import randrange

from pygame import Surface
from pygame.sprite import Sprite, Group

from anim import Animation, AnimationFrames
from spritesheet import SpriteSheet


COIN_SPRITES = None
COIN_FRAMES = None

class CoinAnimation(Animation):
    duration = 35

    def __init__(self):
        global COIN_SPRITES, COIN_FRAMES

        if COIN_SPRITES is None:
            COIN_SPRITES = SpriteSheet("coin", (8, 1))

        if COIN_FRAMES is None:
            COIN_FRAMES = AnimationFrames([
                (self.duration, (0, 0)),
                (self.duration, (1, 0)),
                (self.duration, (2, 0)),
                (self.duration, (3, 0)),
                (self.duration, (4, 0)),
                (self.duration, (5, 0)),
                (self.duration, (6, 0)),
                (self.duration, (7, 0)),
            ])
            # this can be written shorter with list comprehensions as
            # COIN_FRAMES = AnimationFrames([ (self.duration, (i, 0)) for i in range(8) ])

        Animation.__init__(self, COIN_SPRITES, COIN_FRAMES)


## Coin
class Coin(Sprite):
    def __init__(self, loc):
        Sprite.__init__(self)

        self.anim = CoinAnimation()
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

