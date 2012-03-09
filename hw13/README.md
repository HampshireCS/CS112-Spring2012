Homework 15
=========================
Raiden/Shmup
-------------------------

This weekend you will be creating an overhead shooter (aka shoot 'em up aka shmup) similiar to [Raiden](http://www.thenewarcade.com/games/shmup/59/ikaruga).  This game will have a player, bullets, and baddies. 

**Requirements:**
 * The game uses sprites for
    * baddies
    * bullets
    * player
 * at least two enemy types
 * a score


**Things to decide:**
 * do bullets go through enemies or just stop
 * does the player have health or is it a one hit kill


This is a good time to make up points by adding more features to your game.

## Advanced

Create any type of overhead shmup.  It can be like raiden/1942 or more contemporary like geometry wars/everyday shooter. 

Requirements:
 * use spritegroups as well as sprites
 * gameovers and the ability to restart the game after you lose
 * highscore(s)
 * multiple lives
 * multiple weapon types (switchable or collectable)
 * more enemies
    * at least one behaves completely differently than the others
 * a depletable resource.  ex:
    * ammo
    * health
    * shield
 * collectable items.  ex:
    * points
    * new weapons
    * bombs


In addition, add some things to make this game "your own".  Essentially, take the requirements and make it fun to play.  You can change anything as long as it fits within your game design and is still some sort of shooter.  If you skip anything in the above list, try to replace it with something "equivilent" and mention why you skipped it in the instructions.  The point of this class is programming, not artwork. So add more code/logic, not just images.  An example of a "unique" shooter is [Ikaruga](http://www.thenewarcade.com/games/shmup/59/ikaruga), though you don't need to go that far.

> **NOTE:** Make sure to use git or save multiple versions before adding a new feature so you don't irreparably break your programs

Suggestions:
 * use graphics to show what is going on
     * flashing during respawn
     * health meters
 * graphics more complicated than only colored rectangles
     * ie tie fighter complexity
 * powerups
 * health, shields, ammo
 * bombs/other super powers
 * a boss battle
 * terrain
     * change the game to a player running around a room and there are walls
 * more unique enemy types
     * enemies with health
     * spawners
     * enemies that hunt/follow a path
 * a predictable level/levels
 * a way to indicate if an enemy/player was hit
 * AI. ex:
    * hunting enemies
    * [swarm/boid enemies](http://www.red3d.com/cwr/boids/)
 * physics
    * ex: homing missiles actually use thrust

Most importantly, make your game playable and fun.  Lastly, create `INSTRUCTIONS.md` and use [markdown](http://github.github.com/github-flavored-markdown/) to create a decent description, what's included, things to look out for, and clear instructions for playing your game.
