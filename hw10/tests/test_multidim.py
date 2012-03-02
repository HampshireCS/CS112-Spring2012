#!/usr/bin/env python

from base import unittest, not_implemented, test_for

@test_for("multidim.find_coins")
class FindCoinsTest(unittest.TestCase):
    def setUp(self):
        self.empty = [ [0 for i in range(5)] for i in range(5) ]

        self.diag = [ [0 for i in range(5)] for i in range(5) ]
        self.diag[1][1] = 1
        self.diag[3][3] = 1

        self.room = [ [0 for i in range(5)] for i in range(5) ]
        self.room[3][4] = 1
        self.room[0][1] = 1
        self.room[2][2] = 1
        self.room[4][1] = 1


    def test_find_coins_empty(self):
        "room with no coins returns empty list"
        result = multidim.find_coins(self.empty)
        self.assertEqual( len(result), 0)

    def test_find_coins_simple(self):
        "coins on the diagonals"
        result = multidim.find_coins(self.diag)
        result = [ list(r) for r in result ] 
        self.assertItemsEqual(result, [ [1,1], [3,3] ])

    def test_find_coins(self):
        "finds any coin in room"
        result = multidim.find_coins(self.room)
        result = [ list(r) for r in result ] 
        self.assertItemsEqual(result, [ [4,3], [1,0], [2,2], [1,4] ])


@test_for("multidim.distance_from_player")
class DistanceFromPlayerTest(unittest.TestCase):
    def setUp(self):
        self.topleft = [[0.0, 1.0, 2.0, 3.0], [1.0, 1.4142135623730951, 2.2360679774997898, 3.1622776601683795], [2.0, 2.2360679774997898, 2.8284271247461903, 3.6055512754639891], [3.0, 3.1622776601683795, 3.6055512754639891, 4.2426406871192848]]
        self.middle = [[1.4142135623730951, 1.0, 1.4142135623730951, 2.2360679774997898, 3.1622776601683795, 4.1231056256176606, 5.0990195135927845], [1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0], [1.4142135623730951, 1.0, 1.4142135623730951, 2.2360679774997898, 3.1622776601683795, 4.1231056256176606, 5.0990195135927845], [2.2360679774997898, 2.0, 2.2360679774997898, 2.8284271247461903, 3.6055512754639891, 4.4721359549995796, 5.3851648071345037], [3.1622776601683795, 3.0, 3.1622776601683795, 3.6055512754639891, 4.2426406871192848, 5.0, 5.8309518948453007]]


    def test_distance_simple(self):
        "player in the top left"
        self.assertListEqual(self.topleft, multidim.distance_from_player(0, 0, 4, 4))

    def test_distance_middle(self):
        "player at 1,1"
        self.assertListEqual(self.middle, multidim.distance_from_player(1,1,7,5))


if __name__ == "__main__":
    unittest.main()
