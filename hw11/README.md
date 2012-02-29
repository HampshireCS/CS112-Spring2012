Homework 11
===========================
Minesweeper
---------------------------

This week's homework is to implement [minesweeper](http://www.2flashgames.com/f/f-145.htm).  Minesweeper is over when every square is revealed or has a flag on it.  Create a version of minesweeper (graphics can be whatever you want)

Requirements:
 * Right clicking toggles a flag
 * left clicking reveals the square under it
 * different color numbers, a flag, and a bomb graphic
 * show all the unflagged bombs when the player loses

Food for thought:
 * Easy difficulty is fine (10x10 with 10 mines)
 * make sure you don't accidentally place a mine where there already is one
 * calculate how many mines a square is touching before the game starts
 * you don't have to show all the surrounding squares if an empty square is revealed

Don't forget you can get bonus points by doing some of the advanced section stuff or just adding something fancy to your game.


## Advanced

### Minesweeper

Requirements:
 * a way to change the difficulty in game (resizes window)
 * revealing a blank square clears touching squares
 * clicking both mouse buttons clears surrounding squares if conditions are met
     * if a "1" is touching one flag, it clears everything around the 1
 * time how long the game takes
 * don't generate the map until after the first click
     * first click cannot be a mine
 * a "bombs left" counter and time elapsed somewhere on the screen
 * highscore for each difficulty (using shelve is fine)
 * add the smiley face
 * the ability to pause the game
     * when the game is paused, the numbers cannot be visible
 * again, try to make it "unique" somehow

