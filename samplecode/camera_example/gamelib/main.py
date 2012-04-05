import pygame

from gamelib.settings import SCREEN_SIZE
from gamelib.game import Game

def main():
    # initialize pygame
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)

    # create game
    game = Game(screen)
    game.run()
