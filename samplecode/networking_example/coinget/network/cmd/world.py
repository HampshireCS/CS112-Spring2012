from twisted.protocols import amp

from coin import CoinArgument
from player import PlayerArgument

OBJ_ARG = {
    "coin": CoinArgument(),
    "player": PlayerArgument()
}



class WorldObjects(amp.Argument):
    def toBox(self, name, strings, objects, proto):
        for i,obj in enumerate(objects[name]):
            obj_name = "%s%d" % (name, i)
            arg = OBJ_ARG[obj.type]
            strings[obj_name] = obj.type + ":" + arg.toString(obj)


    def fromBox(self, name, strings, objects, proto):
        objs = []

        for key in strings:
            if key.startswith(name):
                typ, data = strings[key].split(":", 1)
                arg = OBJ_ARG[typ]
                objs.append(arg.fromString(data))

        objects[name] = objs


class SyncWorld(amp.Command):
    requiresResponse = True

    arguments = []
    response = [("time", amp.Float()),
                 ("objects", WorldObjects())]


class RemoveObject(amp.Command):
    requiresResponse = False

    arguments = [("identifier", amp.Integer())]
    responce = []
