from louie import dispatcher

from twisted.internet.protocol import ServerFactory
from twisted.protocols import amp

from coinget import signals
from coinget.network import cmd
from coinget.world import Coin, Player

class GameServerProtocol(amp.AMP):
    """
    translates amp requests from client into operations on game world
    """

    def __init__(self, world):
        self.world = world
        self.player = None

        dispatcher.connect(self.add_coin, signal=signals.NEW_OBJECT, sender=Coin)
        dispatcher.connect(self.add_player, signal=signals.NEW_OBJECT, sender=Player)
        dispatcher.connect(self.remove_object, signal=signals.DEL_OBJECT)
        dispatcher.connect(self.move_player, signal=signals.MOVE_PLAYER)

    @cmd.SyncWorld.responder
    def connectionMade(self):
        return { "time": self.world.time,
                 "objects": self.world.objects }

    def connectionLost(self, reason):
        print "lost connection"
        self.world.remove(self.player.identifier)

    def add_coin(self, obj):
        self.callRemote(cmd.AddCoin, coin=obj)

    def add_player(self, obj):
        if obj is not self.player:
            self.callRemote(cmd.AddPlayer, player=obj)
   
    def remove_object(self, sender):
        self.callRemote(cmd.RemoveObject, identifier=sender.identifier)

    @cmd.MovePlayer.responder
    def player_moved(self, identifier, x, y, vx, vy):
        player = self.world.get(identifier)
        dispatcher.send(signal=signals.MOVE_PLAYER, sender=player, x=x, y=y, vx=vx, vy=vy)
        return {}

    def move_player(self, sender, x, y, vx, vy):
        # don't send the move back
        if sender.identifier != self.player.identifier:
            self.callRemote(cmd.MovePlayer, 
                            identifier=sender.identifier, 
                            x=x, 
                            y=y, 
                            vx=vx, 
                            vy=vy)

    @cmd.CreatePlayer.responder
    def create_player(self, nick):
        self.player = self.world.create_player(nick)
        self.world.add(self.player)

        return {"player": self.player}


class GameServerFactory(ServerFactory):
    def __init__(self, world):
        print "server started"
        self.world = world
        self.connections = []

        dispatcher.connect(self.remove_protocol, signals.CONNECTION_CLOSED)
        
    # when player connects, create a new player object
    def buildProtocol(self, addr):
        print addr, "has connected"
        protocol = GameServerProtocol(self.world)

        self.connections.append(protocol)
        return protocol

    def remove_protocol(self, sender):
        if sender in self.connections:
            self.connections.remove(sender)
