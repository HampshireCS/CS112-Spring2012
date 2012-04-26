#!/usr/bin/env python

from coinget.client import GameClient, Options

options = Options(); options.parseOptions()
GameClient(options).start()
