## FILE
import os
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT_DIR, "data")

## GAME
FPS = 60
SCREEN_SIZE = scr_w, scr_h = 400,400

## LEVEL
LEVEL_SIZE = int(1.25 * scr_w), int(1.25 * scr_h)

## PLAYER
PLAYER_SIZE = 30, 30
PLAYER_COLOR = 0,150,0
PLAYER_SPEED = 240


## COINS
COIN_SIZE = 10, 10
COIN_COLOR = 255, 255, 0 
COIN_SPAWN_RATE = 3
COIN_N_STARTING = 30
