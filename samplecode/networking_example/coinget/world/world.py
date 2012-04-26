from collections import defaultdict

from louie import dispatcher
from pygame import Rect

from coinget import settings
from coinget import signals


class World(object):
    def __init__(self, time=0.0):
        self.time = time
        self._objects = {}
        self._objects_by_type = defaultdict(list)

        self.bounds = Rect((0,0), settings.LEVEL_SIZE)

    # provide access to lists of objects by type
    def __getattr__(self, key):
        return self._objects_by_type[key][:]

    @property
    def objects(self):
        return self._objects.values()

    def get(self, identifier):
        return self._objects.get(identifier)

    def add(self, obj):
        self._objects[obj.identifier] = obj
        obj.world = self

        typ = obj.type + "s"
        self._objects_by_type[typ].append(obj)
        dispatcher.send(signal=signals.NEW_OBJECT, sender=obj.__class__, obj=obj)


    def remove(self, identifier):
        if identifier in self._objects:
            obj = self._objects[identifier]
            typ = obj.type + "s"

            del self._objects[identifier]
            self._objects_by_type[typ].remove(obj)
            dispatcher.send(signal=signals.DEL_OBJECT, sender=obj)


    # update the world state based on dt
    def update(self, dt):
        self.time += dt

        for obj in self._objects.values():
            obj.update(dt)


def monitor_add(sender, obj):
    print obj, "added"

def monitor_remove(sender):
    print sender, "removed"

dispatcher.connect(monitor_add, signal=signals.NEW_OBJECT)
dispatcher.connect(monitor_remove, signal=signals.DEL_OBJECT)

