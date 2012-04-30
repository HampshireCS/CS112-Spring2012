from louie import dispatcher
import pygame
from pygame.locals import *

from coinget import signals

from app import Application
from controller import PlayerController
from sprites import *

class ConnectingState(Application.State):
    text = "Connecting..."
    fg = 255,255,255
    bg = 0,0,0

    def setup(self):
        font = pygame.font.Font(None, 50)
        self.text = font.render(self.text, True, self.fg, self.bg)

        self.app.connect(self.connected)

    def connected(self, protocol):
        dispatcher.connect(self.ready, signal=signals.READY, sender=protocol)

    def ready(self, sender):
        player = sender.player
        world = sender.world
        network = sender

        state = GameState(self.app, player, world, network)
        self.app.set_state(state)


    def draw(self, screen):
        screen.fill(self.bg)
        rect = self.text.get_rect()
        bounds = screen.get_rect()
        rect.center = bounds.center
        screen.blit(self.text, rect)
        

class GameState(Application.State):
    def __init__(self, app, player, world, network):
        self.world = world
        self.network = network
        self.player = player
        self.player.local = True

        self.controller = PlayerController(player)

        Application.State.__init__(self, app)

    def setup(self):
        self.coins = CoinGroup()
        for coin in self.world.coins:
            self.coins.add_sprite(coin)

        self.players = PlayerGroup()
        for player in self.world.players:
            self.players.add_sprite(player)

    def handle_event(self, event):
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            self.app.quit()
        else:
            self.controller.handle_event(event)

    def update(self, dt):
        self.world.update(dt)

        self.players.update()
        self.coins.update()
    
    def draw(self, screen):
        screen.fill((80,80,80))
        self.coins.draw(screen)
        self.players.draw(screen)
