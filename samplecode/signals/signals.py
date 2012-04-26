"""
A basic example showing how one might take advantage of using
PyDispatcher/Louie.  To run this example, you must run:
   sudo easy_install louie

Why use signals?  What is this?  for now, start here:  http://pydispatcher.sourceforge.net/
"""

from louie import dispatcher

class Player(object):
    def __init__(self, name):
        self.name = name

        # connect this object's functions to certain signals
        dispatcher.connect(self.move, signal="move_player", sender=self.name)
        dispatcher.connect(self.hear, signal="listen_to")

    def hear(self, sender, message):
        if sender is not self:
            print self.name, "hears", sender.name, "say", message

    def move(self, x, y):
        print "moving", self.name, "to", x, y

    def shout(self, message):
        dispatcher.send(signal="listen_to", message=message, sender=self)

# create a bunch of players
players = [ Player(name) for name in ["Alice", "Bob", "Jack", "Jill"] ]

# moves the proper object
dispatcher.send(signal="move_player", sender="Alice", x=5, y=8)
dispatcher.send(signal="move_player", sender="Alice", x=0, y=2)
dispatcher.send(signal="move_player", sender="Bob", x=-1, y=5)

# does nothing because there is no carol
dispatcher.send(signal="move_player", sender="Carol", x=-1, y=5)

# says the same thing to every player
players[0].shout("Hi guys!")
