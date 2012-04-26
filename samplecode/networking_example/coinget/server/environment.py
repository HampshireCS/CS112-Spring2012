from random import randint, randrange

from pygame import Color

from coinget import rand
from coinget import settings
from coinget.network.clock import SimulationClock
from coinget.world import World
from coinget.world import Coin, Player


class Environment(SimulationClock, World):
    def __init__(self, framerate=1):
        SimulationClock.__init__(self, framerate)
        World.__init__(self)

    def create_player(self, nick):
        bounds = self.bounds.inflate(-self.bounds.width/2, -self.bounds.height/2)
        color = rand.player_color()
        pos = rand.position(bounds)

        return Player(None, nick, color, pos)

    def spawn_coin(self):
        if len(self.coins) < settings.MAX_COINS:
            pos = rand.position(self.bounds)
            coin = Coin(None, pos)
            self.add(coin)

    def advance(self, dt):
        self.update(dt)

        # spawn new coins as needed
        if len(self.coins) == 0:
            self.spawn_coin()



        # check to see if any player has hit any coin
        for player in self.players:
            for coin in self.coins:
                if player.rect.colliderect(coin.rect):
                    self.remove(coin.identifier)
                    self.spawn_coin()
                    self.spawn_coin()
