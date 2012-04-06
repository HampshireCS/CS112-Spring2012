## GAME
FPS = 60
SCREEN_SIZE = scr_w, scr_h = 800,800

## LEVEL
LEVEL_SIZE = int(1.25 * scr_w), int(1.25 * scr_h)

## PLAYER
PLAYER_COLOR = 0,150,0
PLAYER_SPEED = 240


## COINS
COIN_COLOR = 255, 255, 0 
COIN_SPAWN_RATE = 0.5
COIN_N_STARTING = 30
COIN_SPEED = PLAYER_SPEED * 2/3.0   # 2/3 player speed
COIN_ACCEL = COIN_SPEED / 5         # 5 seconds to get up to speed
COIN_SPAWN_COUNT = 4
