from random import randint, randrange

from pygame import Color

def player_color():
    color = [ randrange(128,256) for _ in range(3) ]

    num_channels = randint(1,2)
    for i in range(num_channels):
        channel = randrange(3)
        color[channel] = 0

    return Color(*color)


def position(bounds):
    x = randrange(bounds.width)
    y = randrange(bounds.height)
    return bounds.x + x, bounds.y + y


