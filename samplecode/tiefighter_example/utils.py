from random import randint, random

import pygame

def rand_odds(n,t):
    n = n / float(t)
    return random() < n


def randint_neg(lo,hi):
    r = randint(lo,hi)
    sign = randint(0,1) * 2 - 1
    return r * sign


def collide_rect_circle(rect, pos, radius):
    cx, cy = pos
    rx, ry = rect.center

    w = rect.width/2.0
    h = rect.height/2.0
    cdx = abs(cx - rect.centerx)
    cdy = abs(cy - rect.centery)

    if cdx > w+radius or cdy > h+radius:
        return False

    if cdx <= w or cdy <= h:
        return True

    corner = (cdx - w)**2 + (cdy-h)**2

    return corner <= radius**2

