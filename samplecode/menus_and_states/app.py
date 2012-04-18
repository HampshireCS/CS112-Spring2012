import inspect

import pygame
from pygame.locals import *

class ApplicationState(object):
    def __init__(self, app):
        self.app = app
        self.setup()

    def setup(self): pass
    def resume(self): pass
    def handle_event(self, event): pass
    def update(self): pass
    def draw(self, screen): pass


class Application(object):
    def __init__(self, state):
        self.screen = pygame.display.get_surface()
        pygame.display.set_caption("Super Coin Get")

        self.set_state(state)

    def quit(self):
        self.done = True

    def set_state(self, state):
        if inspect.isclass(state):
            state = state(self)

        state.resume()
        self.state = state

    def run(self):
        self.done = False
        while not self.done:
            # input
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.quit()
                else:
                    self.state.handle_event(event)

            self.state.update()
            self.state.draw(self.screen)
            pygame.display.flip()

