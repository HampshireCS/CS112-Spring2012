#!/usr/bin/env python

import pygame

def colorkey(color):
    if color == (0,0,0):
        return (255,255,255)
    else:
        return (0,0,0)

def clear(surf, color):
    ck = colorkey(color)
    surf.fill(ck)
    surf.set_colorkey(ck)


def draw_tie(surf, color):
    clear(surf, color)
    rect = surf.get_rect()

    d = min(rect.width, rect.height)
    wall = d/8

    dw = rect.width - d
    dh = rect.height - d

    pygame.draw.rect(surf, color, (0, 0, wall, rect.height))
    pygame.draw.rect(surf, color, (rect.right-wall, 0, wall, rect.height))
    pygame.draw.rect(surf, color, (0, (rect.height - wall)/2, rect.width, wall))
    pygame.draw.circle(surf, color, ( (d+dw)/2, (d+dh)/2 ), d / 4)
    

def draw_ywing(surf, color):
    clear(surf, color)
    rect = surf.get_rect()

    unit = rect.height / 16
    engine_len = rect.width / 2 + 3 * unit
    
    pygame.draw.rect(surf, color, (0, 0, engine_len + unit, 3 * unit))
    pygame.draw.rect(surf, color, (0, rect.height - 3*unit, engine_len + unit, 3 * unit))
    pygame.draw.rect(surf, color, (rect.width-engine_len, (rect.height - 3*unit) / 2, engine_len, 3 * unit))
    pygame.draw.rect(surf, color, ( (rect.width - 3*unit)/2, 0, 3 * unit, rect.height))
    pygame.draw.rect(surf, color, ( rect.width - 9*unit, (rect.height - 6*unit)/2, 9 * unit, 6*unit))
