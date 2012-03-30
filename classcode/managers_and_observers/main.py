#!/usr/bin/env python

import pygame
from pygame.locals import *

from core.input import InputManager, KeyListener, MouseListener

# world/player.py
class Player(object):
    def move(self, direction):
        print "player moves %d, %d" % direction

    def jump(self):
        print "player jumps"


# core/sound.py
class SoundManager(object):
    def play(self, which):
        print "playing %s sound" % which


# controls/player.py
class PlayerController(KeyListener, MouseListener):
    def __init__(self, player):
        self.player = player

    def on_keydown(self, event):
        if event.key == K_SPACE:
            self.player.jump()

    def on_motion(self, event):
        self.player.move( event.rel )



# controls/sound.py
class SfxController(KeyListener):
    def __init__(self, sm, game):
        self.game = game
        self.sm = sm

    def on_keydown(self, event):
        if self.game.paused():
            return

        if event.key == K_SPACE:
            self.sm.play("jump")

        if event.key == K_c:
            self.sm.play("slash")



class Game(object):
    size = 800, 600

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)

        self.input = InputManager()

        self.player = Player()
        self.sounds = SoundManager()
        
        pc = PlayerController(self.player)
        self.input.add_key_listener(pc)
        self.input.add_mouse_listener(pc)

        sc = SfxController(self.sounds, self)
        self.input.add_key_listener(sc)

    def paused(self):
        return False


    def quit(self):
        self._done = True

    def run(self):
        self._done = False

        while not self._done:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.quit()
                else:
                    self.input.handle_event(event)

        # update

        # draw
        self.screen.fill((0,0,0))
        pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run()
