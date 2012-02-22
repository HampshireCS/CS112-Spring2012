#!/usr/bin/env python
import unittest

from adv_nims import *

class ParserFunctions(unittest.TestCase):
    def test_splitparts_basic(self):
        self.assertEquals(splitparts(""), [], "can't handle empty strings")
        self.assertEquals(splitparts("a"), ["a"], "can't handle single values")
        self.assertEquals(splitparts("1"), ["1"], "can't handle single values")
        self.assertEquals(splitparts("a 1"), ["a", "1"], "can't handle simple spaces")
        self.assertEquals(splitparts("a,2"), ["a", "2"], "can't handle simple commas")

    def test_splitparts_multi(self):
        self.assertEquals(splitparts("1 2 3 3 2"), ["1","2","3","3","2"], "can't handle multiple values")
        self.assertEquals(splitparts("1,2,3,2,3"), ["1","2","3","2","3"], "can't handle multiple values")

    def test_splitparts_complicated(self):
        self.assertEquals(splitparts("a, 3"), ["a", "3"], "can't handle spaces and commas")
        self.assertEquals(splitparts("A  3"), ["A", "3"], "can't handle multiple spaces")
        self.assertEquals(splitparts("A,  3, 4 , 6"), ["A", "3", "4", "6"], "can't handle crazy input")
        self.assertEquals(splitparts("  A  3  4    "), ["A", "3", "4"], "can't handle leading/trailing spaces")
        self.assertEquals(splitparts(",,a,b,,c,,"), ["a","b","c"], "can't handle crazy input")
        self.assertEquals(splitparts(",a,b ,c ,,e ,  "), ["a","b","c","e"], "can't handle crazy input")

    def test_parse_stones(self):
        self.assertEquals(parse_stones("1 2"), [1,2])
        self.assertEquals(parse_stones("-1 4"), [4], "no negative numbers")
        self.assertEquals(parse_stones("0 4"), [4], "no zeros")
        self.assertEquals(parse_stones("100 43"), [99,43], "max out at 99")


class HelperTests(unittest.TestCase):
    def test_a2idx(self):
        self.assertEquals(a2idx("A"), 0)
        self.assertEquals(a2idx("a"), 0)
        self.assertEquals(a2idx("z"), 25)

    def test_idx2a(self):
        self.assertEquals(idx2a(0), "A")
        self.assertEquals(idx2a(25), "Z")


class OutputTests(unittest.TestCase):
    def test_header(self):
        self.assertEquals(header(range(1)), " A | Move")
        self.assertEquals(header(range(2)), " A  B | Move")
        self.assertEquals(header(range(5)), " A  B  C  D  E | Move")

    def test_separater(self):
        self.assertEquals(separater(range(1)), "-" * 22, "expected 22 -")
        self.assertEquals(separater(range(2)), "-" * 25, "expected 25 -")
        self.assertEquals(separater(range(5)), "-" * 34, "expected 34 -")

    def test_prompt(self):
        self.assertEquals(prompt([10,0], 0), "10  0 | Player 1:  ")
        self.assertEquals(prompt([0,0], 1), " 0  0 | Player 2:  ")
        self.assertEquals(prompt([12,15,3], 1), "12 15  3 | Player 2:  ")


class MoveTests(unittest.TestCase):
    def test_parse_move(self):
        self.assertEqual(parse_move("A 3"), (0, 3))
        self.assertEqual(parse_move("d 0"), (3, 0))
        self.assertEqual(parse_move("z 32"), (25, 32))

    def test_parse_move_errors(self):
        self.assertFalse(parse_move(""), "empty input")
        self.assertFalse(parse_move("a"), "missing amount")
        self.assertFalse(parse_move("3"), "missing pile")
        self.assertFalse(parse_move("1 3"), "invalid pile")
        self.assertFalse(parse_move("4 a"), "swapped valuse")
        self.assertFalse(parse_move("$ 9"), "invalid pile")
        self.assertFalse(parse_move("a 3.4"), "invalid amount: fraction")

    def test_valid_move(self):
        self.assertFalse(valid_move(None, []), "must handle None")
        self.assertFalse(valid_move((0, -3), [1]), "invalid amount: negative")
        self.assertFalse(valid_move((0, 0), [1]), "invalid amount: zero")
        self.assertFalse(valid_move((3, 3), [4,5]), "invalid pile, out of range")
        self.assertFalse(valid_move((0, 7), [4,5]), "not enough stones left")
        self.assertTrue(valid_move((0, 3), [4,5]), "valid move")

    def test_move(self):
        piles = [4,5]
        move((1,3), piles)
        self.assertEquals(piles, [4,2])

if __name__ == "__main__":
    unittest.main()
