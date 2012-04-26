from twisted.internet import reactor
from twisted.internet.endpoints import TCP4ClientEndpoint
from twisted.python import usage

import pygame

from coinget import settings

from app import Application
from game import ConnectingState
from network import NetworkControllerFactory


class Options(usage.Options):
    optParameters = [
        ("port", "p", settings.DEFAULT_PORT, "TCP port", usage.portCoerce),
        ("nick", "n", "Anon", "Nickname"),
        ("addr", "s", "localhost", "Server address")
    ]


class GameClient(Application):
    def __init__(self, options):
        pygame.init()
        pygame.display.set_mode(settings.SCREEN_SIZE)
        pygame.display.set_caption(settings.CAPTION)

        self.nick = options["nick"]
        self.addr = options["addr"]
        self.port = options["port"]

        self.factory = NetworkControllerFactory(self)
        Application.__init__(self, ConnectingState)


    def connect(self, callback=None):
        endpt = TCP4ClientEndpoint(reactor, self.addr, self.port)
        d = endpt.connect(self.factory)
        if callback:
            d.addCallback(callback)

    def start(self):
        Application.start(self)
        reactor.run()

    def quit(self):
        Application.quit(self)
        pygame.quit()
        reactor.stop()
