import pygame

from app import Application
from game import MainMenu

def main():
    # initialize pygame
    pygame.init()
    pygame.display.set_mode((800, 800))

    # create game
    app = Application(MainMenu)
    try:
        app.run()
    except KeyboardInterrupt:
        app.quit()

if __name__ == "__main__":
    main()
