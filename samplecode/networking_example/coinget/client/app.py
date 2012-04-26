import inspect

from louie import dispatcher
import pygame
from pygame.locals import *


from coinget import signals
from coinget.network.clock import SimulationClock


class Application(SimulationClock):
    framerate = 60
    state = None

    def __init__(self, state=None):
        SimulationClock.__init__(self, framerate=self.framerate)
        self.screen = pygame.display.get_surface()

        # initialize base state
        if state is None:
            state = Application.State

        self.set_state(state)

        # connect signals
        dispatcher.connect(self.quit, sender=self, signal=signals.QUIT)
    
    def quit(self):
        self.stop()

    def set_state(self, state):
        if self.state:
            self.state.pause()

        if inspect.isclass(state):
            state = state(self)

        state.resume()
        self.state = state

    
    def advance(self, dt):
        for event in pygame.event.get():
            if event.type == QUIT:
                dispatcher.send(signal=signals.QUIT, sender=self)
            else:
                self.state.handle_event(event)

        self.state.update(dt)
        self.state.draw(self.screen)
        pygame.display.flip()


    class State(object):
        def __init__(self, app):
            self.app = app
            self.setup()

        def setup(self): pass
        def pause(self): pass
        def resume(self): pass
        def handle_event(self, event): pass
        def update(self, dt): pass
        def draw(self, screen): pass

"""
class GameApp(World):
    fps = 1

    def __init__(self):
        World.__init__(self, framerate=self.fps)

        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))

        self.background = TiledImage(load_image("grass"))

        
    def quit(self):
        self.stop()
        pygame.quit()

    def draw(self, screen):

        self.background.draw(screen)

    def advance(self, dt):
        for event in pygame.event.get():
            if event.type == QUIT:
                dispatcher.send(signal=signals.QUIT)

        World.advance(self, dt)
        self.draw(self.screen)
        pygame.display.flip()
"""
