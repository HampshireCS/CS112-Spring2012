#!/usr/bin/env python

try:
    from points import Point
    no_point = False
except ImportError:
    class Point(object):
        def __init__(self, *a):
            pass
    no_point = True


try:
    import unittest2 as unittest
except ImportError:
    import unittest

@unittest.skipIf(no_point, "Point class is not implemented")
class PointTest(unittest.TestCase):

    def test_init(self):
        pt = Point(3,4)
        self.assertTrue(hasattr(pt, 'x'), "point missing 'x' attribute")
        self.assertTrue(hasattr(pt, 'y'), "point missing 'y' attribute")
        self.assertEqual(pt.x, 3, "point has incorrect 'x' value")
        self.assertEqual(pt.y, 4, "point has incorrect 'y' value")

    @unittest.skipIf(not hasattr(Point, "distance"), "Point has no distance method")
    def test_distance(self):
        a = Point(0,0)
        b = Point(3,4)
        c = Point(2,0)

        error_msg1 = "incorrect distance between (%d, %d) and (%d, %d)" % (a.x, a.y, c.x, c.y)
        error_msg2 = "incorrect distance between (%d, %d) and (%d, %d)" % (a.x, a.y, b.x, b.y)
        self.assertEqual(a.distance(c), 2, error_msg1)
        self.assertEqual(a.distance(b), 5, error_msg2)


    @unittest.skipIf(not hasattr(Point, "move"), "Point has no move method")
    def test_move(self):
        pt = Point(4,5)
        pt.move(2,3)

        self.assertEqual(pt.x, 2, "pt.x did not move from 4 to 2")
        self.assertEqual(pt.y, 3, "pt.y did not move from 5 to 3")

    @unittest.skipIf(not hasattr(Point, "translate"), "Point has no translate method")
    def test_translate(self):
        pt = Point(4,5)
        pt.translate(-1, 1)
        self.assertEqual(pt.x, 3, "pt.x did not translate by -1 from 4 to 3")
        self.assertEqual(pt.y, 6, "pt.y did not translate by 1 from 5 to 6")


    @unittest.skipIf(not hasattr(Point, "slope"), "Point has no slope method")
    def test_slope(self):
        a = Point(1,1)
        b = Point(2,2)
        self.assertEqual(a.slope(b), 1, "incorrect slope between (%d, %d) and (%d, %d)" % (a.x, a.y, b.x, b.y))

        a = Point(1,1)
        b = Point(2,3)
        self.assertEqual(a.slope(b), 2, "incorrect slope between (%d, %d) and (%d, %d)" % (a.x, a.y, b.x, b.y))

        a = Point(1,1)
        b = Point(3,2)
        self.assertEqual(a.slope(b), 0.5, "incorrect slope between (%d, %d) and (%d, %d)" % (a.x, a.y, b.x, b.y))

        a = Point(5,3)
        b = Point(6,2)
        self.assertEqual(a.slope(b), -1, "incorrect slope between (%d, %d) and (%d, %d)" % (a.x, a.y, b.x, b.y))

        a = Point(5,3)
        b = Point(4,3)
        self.assertEqual(a.slope(b), 0, "incorrect slope between (%d, %d) and (%d, %d)" % (a.x, a.y, b.x, b.y))

        a = Point(5,3)
        b = Point(5,0)
        self.assertIsNone(a.slope(b), "incorrect slope between (%d, %d) and (%d, %d)" % (a.x, a.y, b.x, b.y))


if __name__ == "__main__":
    unittest.main(verbosity=2)
