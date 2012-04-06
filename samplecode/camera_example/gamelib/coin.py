import math
from random import randrange

from pygame import Surface
from pygame.sprite import Sprite, Group

from settings import COIN_COLOR, COIN_SPAWN_RATE, COIN_SPEED, COIN_ACCEL, COIN_SPAWN_COUNT

class Coin(Sprite):

    def __init__(self, loc):
        Sprite.__init__(self)

        self.image = Surface((30, 30))
        self.rect = self.image.get_rect()

        self.image.fill((0,0,0))
        self.image.fill(COIN_COLOR, self.rect.inflate(-2, -2))
        self.rect.center = loc
        self.vel = 0

        self.x = self.rect.centerx
        self.y = self.rect.centery


    def move_toward(self, target, dt):
        dt /= 1000.0
 
        self.vel += dt * COIN_ACCEL
        if self.vel > COIN_SPEED:
            self.vel = COIN_SPEED
        
        x, y = self.x, self.y
        tx, ty = target.rect.center
        dx, dy = tx - x, ty - y

        # calculate the parts of the ang vel
        if tx == x:
            vx = 0
            vy = self.vel
        else:
            theta = math.atan( (ty-y) / (tx - x) )
            vx = math.copysign(self.vel * math.cos(theta), dx)
            vy = math.copysign(self.vel * math.sin(theta), dy)

        self.x += vx * dt
        self.y += vy * dt

        self.rect.center = int(self.x), int(self.y)



class CoinGroup(Group):
    def __init__(self, bounds):
        Group.__init__(self)

        self.bounds = bounds

        self.spawn_rate = COIN_SPAWN_RATE * 1000
        self.spawn_timer = 0

    def spawn(self):
        x = randrange(self.bounds.x, self.bounds.x + self.bounds.width)
        y = randrange(self.bounds.y, self.bounds.y + self.bounds.height)

        coin = Coin((x,y))
        coin.rect.clamp_ip(self.bounds)
        self.add(coin)

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer >= self.spawn_rate:
            for i in range(COIN_SPAWN_COUNT):
                self.spawn()
            self.spawn_timer = 0


