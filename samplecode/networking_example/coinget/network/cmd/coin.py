import struct

from twisted.protocols import amp

from coinget.world import Coin

class CoinArgument(amp.Argument):
    frmt = "!iiif"

    def toString(self, coin):
        identifier = coin.identifier
        x,y = coin.rect.center
        life = coin.life

        return struct.pack(self.frmt, identifier, x, y, life)

    def fromString(self, encoded):
        identifier, x, y, life = struct.unpack(self.frmt, encoded)
        coin = Coin(identifier, (x,y))
        coin.life = life
        return coin
        
class AddCoin(amp.Command):
    requiresResponce = False
    arguments = [("coin", CoinArgument())]
    responce = []

class CollectCoin(amp.Command):
    requiresResponce = False

    arguments = [("player_id", amp.Integer()),
                 ("coin_id", amp.Integer()),
                 ("score", amp.Integer())]
