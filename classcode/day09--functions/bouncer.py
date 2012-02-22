import pygame
from pygame import draw
from random import randrange
from pygame.locals import *

tie_x, tie_y = 400,300

def draw_tie(surf, pos, color=(255,0,0), size=40):
    "Draws a tie fighter"
    x,y = pos
    
    width = size/8

    draw.rect(surf, color, (x, y, width, size))
    draw.rect(surf, color, (x+(size-width), y, width, size))
    draw.rect(surf, color, (x, y+(size-width)/2, size, width))
    draw.circle(surf, color, (x+size/2, y+size/2), size/4)

pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True

    screen.fill((0,0,0))
    draw_tie(screen, [tie_x, tie_y])
    
    pygame.display.flip()
    clock.tick(30)
    
print "ByeBye"
