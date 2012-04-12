#!/usr/bin/env python

from math import ceil, floor

import pygame
from pygame.locals import *

from pygame import Rect

from quad import QuadTreeNode


pygame.init()
screen = pygame.display.set_mode((800, 800))
root = QuadTreeNode(screen.get_rect())

done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True
        elif event.type == MOUSEBUTTONDOWN:
            root.add_point(pygame.mouse.get_pos())

    screen.fill(0)

    # draw quadtree
    if hasattr(root, "collidepoint"):
        active = root.collidepoint(pygame.mouse.get_pos())
        screen.fill((80,80,80), active.rect)

    if hasattr(root, "get_rects"):
        for rect in root.get_rects():
            pygame.draw.rect(screen, (170, 170, 170), rect, 1)

    if hasattr(root, "get_points"):
        for point in root.get_points():
            pygame.draw.circle(screen, (255,255,255), point, 3)

    pygame.display.flip()
    clock.tick(30)
