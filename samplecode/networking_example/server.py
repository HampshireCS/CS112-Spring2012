#!/usr/bin/env python
from coinget.server import GameServer, Options


options = Options(); options.parseOptions()
server = GameServer(options)
server.start()

