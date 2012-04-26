from twisted.internet import reactor
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.python import usage

from environment import Environment
from network import GameServerFactory

from coinget import settings

class Options(usage.Options):
    optParameters = [
        ('port', 'p', settings.DEFAULT_PORT, "TCP port number to listen on.", usage.portCoerce)
    ]

    
class GameServer(object):
    def __init__(self, options):
        self.port = options['port']

    def start(self):
        environment = Environment(framerate=15)
        factory = GameServerFactory(environment)

        endpt = TCP4ServerEndpoint(reactor, self.port)
        endpt.listen(factory)

        environment.start()

        reactor.run()
