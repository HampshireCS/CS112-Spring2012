from twisted.internet import reactor
from twisted.internet.task import LoopingCall, Clock

# our new "game loop"
class SimulationClock(Clock):
    _call = None

    def __init__(self, framerate):
        Clock.__init__(self)
        self.framerate = framerate


    def _update(self, frames):
        self.advance(1.0 * frames / self.framerate)


    def start(self):
        """
        Start the simulated advancement of time.
        """
        self._call = LoopingCall.withCount(self._update)
        self._call.clock = reactor
        self._call.start(1.0 / self.framerate, now=False)
        self._running = True


    def stop(self):
        """
        Stop the simulated advancement of time. Clean up all pending calls.
        """
        if self._running:
            self._running = False
            self._call.stop()
