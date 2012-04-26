## SETUP louie, also imports dispatcher so importing modules just need this one
import louie
louie.plugin.install_plugin( louie.plugin.TwistedDispatchPlugin() )

# App signals
QUIT = "QUIT"
READY = "READY"

CONNECTION_CLOSED = "CONNECTION_CLOSED"

NEW_OBJECT = "NEW_OBJECT"
DEL_OBJECT = "DEL_OBJECT"

MOVE_PLAYER = "MOVE_PLAYER"
COLLECT_COIN = "COLLECT_COIN"

