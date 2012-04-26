import struct

import pygame
from twisted.protocols import amp

from coinget.world import Player


def take(n, arr):
    result = []
    for i in range(n):
        result.append( arr.pop(0) )
    return result


class PlayerArgument(amp.Argument):
    def toString(self, player):
        frmt = "!";    data = []
        frmt += "i";   data += [player.identifier]
        frmt += "BBB"; data += player.color[:3]
        frmt += "ii";  data += player.rect.center
        frmt += "ii";  data += [ player.vx, player.vy]
        frmt += "s";   data += [ player.nick ]

        return struct.pack(frmt, *data)

    def fromString(self, encoded):
        frmt = "!iBBBiiiis"
        data = list(struct.unpack(frmt, encoded))

        identifier = take(1, data)[0]
        color = take(3, data)
        pos = take(2, data)
        vel = take(2, data)
        nick = take(1, data)[0]

        color = pygame.Color(*color)

        return Player(identifier, nick, color, pos, vel)


class CreatePlayer(amp.Command):
    requiresResponse = True
    arguments = [("nick", amp.String())]
    response = [("player", PlayerArgument())]


class AddPlayer(amp.Command):
    requiresResponse = False
    arguments = [("player", PlayerArgument())]
    response = []

class MovePlayer(amp.Command):
    requiresResponse = False
    arguments = [("identifier", amp.Integer()),
                 ("x", amp.Integer()),
                 ("y", amp.Integer()),
                 ("vx", amp.Integer()),
                 ("vy", amp.Integer())]
    response = []
