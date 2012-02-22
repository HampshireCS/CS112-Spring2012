#!/usr/bin/env python

###################### 
#  Helper Functions
######################

def splitparts(s):
    "split_ints takes a string and returns all chunks.  Chunks are any space separated or comma separated values"
    
def a2idx(c):
    "converts a letter to it's index value"

def idx2a(i):
    "converts an index to it's letter value"

##############################################
# Object Functions
#    functions relating to moves and stones
###############################################

def parse_stones(s):
    """given a list of nums (chunks) return a list of stone piles.  Piles cannot be less than 0
    and can be a maximum of 99 stones

    >>> parse_stones("12, 13")
    [12, 13]
    >>> parse_stones("0 200 4 5")
    [99, 4 5]
    """

# moves are [pile, amount] => [int, int]

def parse_move(s):
    """given an attempted move, parse the input into a "move list"

    >>> parse_move("A  3")
    [0, 3]
    >>> parse_move("this isn't valid")
    None
    """

def valid_move(mv, piles):
    """check if a given move can actually be completed

    >>> valid_move(None, [3,3])
    False
    >>> valid_move([0,3], [3,3])
    True
    >>> valid_move([1,20], [3,3])
    False
    >>> valid_move([20,2], [3,3])
    False
    """


def move(mv, piles):
    "perform a move"

#####################################
#  Output Functions
#     functions which format strings
#####################################
def header(piles):
    "draw the header of the game table"

def prompt(piles, player):
    "format the input prompt"

# do not touch, already done
def separater(piles):
    "creates a separater under the header, long enough to cover all the piles"
    total = 21 + len(piles)
    total += (len(piles) - 1) * 2
    return "=" * total

###########################################
#  MAIN -- DO NOT TOUCH BELOW THIS POINT 
###########################################
def main():
    piles = parse_stones(raw_input("Number of stones in each pile:  "))
    print ""

    print header(piles)
    print separater(piles)

    # init 
    player = 0      # player will be 0 or 1

    # loop as long as any value in piles != 0
    while any(piles): 
        inp = parse_move( raw_input(prompt(piles, player)) )

        # check for valid input
        if not valid_move(inp, piles):
            print "*Error*  Invalid Move"
            continue

        move(inp, piles)
        player = (player + 1) % 2

    # declare winner
    print "Player %d wins!!!" % (player + 1)

if __name__ == "__main__":
    main()
