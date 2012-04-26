def id_generator():
    c = 0
    while True:
        yield c
        c += 1


class WorldObject(object):
    ids = id_generator()
    identifier = None

    def __init__(self, identifier):
        if identifier is None:
            identifier = WorldObject.ids.next()
        self.identifier = identifier

    @property
    def type(self):
        return self.__class__.__name__.lower()

    def kill(self):
        self.world.remove(self.identifier)

    def update(self, dt):
        pass
