#!/usr/bin/env python

import pygame
from pygame.locals import *

pygame.init()

# dimensions of each sprite frame (this is known ahead of time)
WIDTH = 240
HEIGHT = 296

# load images
screen = pygame.display.set_mode((WIDTH, HEIGHT))
image = pygame.image.load("spritesheet.bmp").convert()

# loop through the sprite sheet and create "subsurfaces" for each portion of the image
images = []
for x in range(6):
    for y in range(5):
        images.append(image.subsurface((x*WIDTH, y*HEIGHT, WIDTH, HEIGHT)))

# init
idx = 0
clock = pygame.time.Clock()
done = False
while not done:
    for evt in pygame.event.get():
        if evt.type == QUIT:
            done = True
        elif evt.type == KEYDOWN and evt.key == K_ESCAPE:
            done = True

    # draw
    screen.blit(images[idx], (0,0))
    pygame.display.flip()
    clock.tick(10)
    idx += 1
    idx %= len(images) - 1
