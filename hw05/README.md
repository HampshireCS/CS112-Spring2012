Homework 5
===================
Basic Software
-------------------

## nims.py
Nims is a classic game where players take turns taking stones off of a pile.  Whoever takes that last stone is the loser.  When you run the program, it should look as close as possible to bellow.

```
$ python nims.py
Number of stones in the pile:  40
Max number of stones per turn: 5

40 stones left.  Player 1 [1-5]:  5
35 stones left.  Player 2 [1-5]:  4
31 stones left.  Player 1 [1-5]:  5
26 stones left.  Player 2 [1-5]:  6
Invalid number of stones
26 stones left.  Player 2 [1-5]:  5
21 stones left.  Player 1 [1-5]:  5
16 stones left.  Player 2 [1-5]:  5
11 stones left.  Player 1 [1-5]:  1
10 stones left.  Player 2 [1-5]:  1
9 stones left.  Player 1 [1-5]:  3
6 stones left.  Player 2 [1-5]:  1
5 stones left.  Player 1 [1-5]:  4
1 stones left.  Player 2 [1-5]:  3
Not enough stones
1 stones left.  Player 2 [1-5]:  1
Player 1 wins!!!
```

## rings.py
Draw the olympic rings. See the example image bellow.


----

# Advanced

## nims.py
Instead of one pile, implement nims to have N piles.  Whoever takes the absolute last stone is still the loser.  It work like the code bellow.

```
$ python nims.py
Number of stones in each pile:  12 14 15 9

 A  B  C  D | Move
-------------------------------
12 14 15  9 | Player 1:  A 11
 1 14 15  9 | Player 2:  A 3
*Error*  Not enough stones
 1 14 15  9 | Player 2:  D 7
 1 14 15  2 | Player 1:  B 11
 1  3 15  2 | Player 2:  C 13
 1  3  2  2 | Player 1:  A 1
 0  3  2  2 | Player 2:  D 2
 0  3  2  0 | Player 1:  B 1
 0  2  2  0 | Player 2:  C 1
 0  2  1  0 | Player 1:  B 2
 0  0  1  0 | Player 2:  C 1

Player 1 wins!!!
```

## rings.py
In addition to just drawing the olympic rings, make sure they overlap properly.  See the example image bellow.


## tictactoe.py
Program tic tac toe.  It can be graphical or text.  There can be AI or just two player.  The only requirement is the program has to be tic tac toe and it has to be able to tell when someone wins.


## lists.py
Finish all the problems in `lists.py`.  Each question only requires a single python statement.

----

# Rings Examples
> **Basic Rings:**
> ![Image](https://github.com/HampshireCS/CS112-Spring2012/raw/master/hw05/example_rings_basic.png)
>
> **Advanced Rings:**
> ![Image](https://github.com/HampshireCS/CS112-Spring2012/raw/master/hw05/example_rings_adv.png)
