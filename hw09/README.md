===================
Homework 9
===================
Tron
-------------------

This weekend, take a stab at programming the game [tron](http://www.classicgamesarcade.com/game/21670/tron-game.html).  It doesn't have to be fancy, just a simple game of red vs blue.

### Requirements

 * create the game tron for 2 players
 * control the players with WSAD and arrow keys
 * start the game when the spacebar is pressed
 * **BONUS** make it so when the game is over, you can reset it with space

### Hints

 * both players leave a trail.  This trail is kinda like a list of cells they take up
 * the way you draw and track each player should be the same.  You could probably do some functions.
 * you can create constants that can make life easier:
 * if you store points in a list, you can probably check to see if a point is already there with `in`.

```python
RED = 255,0,0

# ...snip...

NORTH = 1
SOUTH = 2

# ...snip...

PLAYING = 1
GAMEOVER = 2

# ...snip...
```
## Advanced

There will be more pieces updated after class tomorrow with some more excercises.  In addition to the basic tron, include the following.

 * make the game single player (blue player has AI).  This AI can be incredibly niave, one step above random.
 * player paths have a black outline around them
 * some sort of "explosion" graphic/drawing where the player hits to indicate a game over
 * the game can be reset and restarted (not just a bonus for you)
 * paint the score somewhere to the screen before the game starts
 * make it look kindy fancy.
