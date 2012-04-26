from louie import dispatcher

from twisted.internet.protocol import ReconnectingClientFactory
from twisted.protocols import amp

from coinget import signals
from coinget.network import cmd
from coinget.world import World, Coin, Player

class NetworkController(amp.AMP):
    world = None

    def __init__(self, nick):
        self.nick = nick
        dispatcher.connect(self.quit, signal=signals.QUIT)
        dispatcher.connect(self.move_player, signal=signals.MOVE_PLAYER)

    def connectionMade(self):
        self.sync_world()

    def connectionLost(self, reason):
        print "Connection with server has been lost"

    def quit(self, sender, signal):
        if sender is not self:
            self.transport.loseConnection()

    def create_player(self):
        d = self.callRemote(cmd.CreatePlayer, nick=self.nick)
        d.addCallback(self.player_created)
        return d

    def player_created(self, result):
        self.player = result["player"]
        self.world.add(self.player)
        self.ready()

    def move_player(self, sender, x, y, vx, vy):
        # only send off if we actually have control
        if sender is self.player:
            self.callRemote(cmd.MovePlayer, identifier=sender.identifier, x=x, y=y, vx=vx, vy=vy)

    @cmd.MovePlayer.responder
    def player_moved(self, identifier, x, y, vx, vy):
        player = self.world.get(identifier)
        dispatcher.send(signal=signals.MOVE_PLAYER, sender=player, x=x, y=y, vx=vx, vy=vy)
        return {}


    def sync_world(self):
        self.callRemote(cmd.SyncWorld).addCallback(self.load_world)
    
    def load_world(self, result):
        self.world = World()
        for obj in result["objects"]:
            self.world.add(obj)
        self.world.time = result["time"]
        self.create_player()

    def ready(self):
        dispatcher.send(signal=signals.READY, sender=self)

    @cmd.AddCoin.responder
    def add_coin(self, coin):
        self.world.add(coin)
        return {}

    @cmd.AddPlayer.responder
    def add_player(self, player):
        self.world.add(player)
        return {}

    @cmd.RemoveObject.responder
    def remove_object(self, identifier):
        self.world.remove(identifier)
        return {}

class NetworkControllerFactory(ReconnectingClientFactory):
    def __init__(self, app):
        self.app = app

    def buildProtocol(self, addr):
        # create a new world for the appstate once connceted

        print "Connected"
        self.resetDelay()
        return NetworkController(self.app.nick)

    # close down reactor on disconnect
#    def clientConnectionLost(self, connector, reason):
#        dispatcher.send(signal=signals.QUIT, sender=connector)
