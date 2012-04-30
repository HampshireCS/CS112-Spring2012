from random import randint, randrange

from pygame import Color

def player_color():
    color = [ 0, 0, 0 ]
    for i in range(randrange(1,3)):
        channel = randrange(3)
        color[channel] = randrange(128,256)

    return Color(*color)


def position(bounds):
    x = randrange(bounds.width)
    y = randrange(bounds.height)
    return bounds.x + x, bounds.y + y


