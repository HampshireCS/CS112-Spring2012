#!/usr/bin/env python

from base import unittest, not_implemented, test_for

from pygame import Rect

@test_for("rects.poly_in_rect")
class PolyInRectsTest(unittest.TestCase):
    def setUp(self):
        self.rect = Rect(0,0,10,10)
        self.poly_inside = [ (2,2), (4,4), (3,2) ]
        self.poly_partial = [ (2,2), (4,4), (3,2), (-1,20) ]
        self.poly_outside = [ (32,2), (34,4), (33,2) ]

    def test_poly_in_rect_inside(self):
        "works with poly fully inside"
        self.assertTrue( rects.poly_in_rect(self.poly_inside, self.rect), "%r should be inside %r" % (self.poly_inside, self.rect))

    def test_poly_in_rect_partial(self):
        "fails with one point outside"
        self.assertFalse( rects.poly_in_rect(self.poly_partial, self.rect), "%r should be inside %r" % (self.poly_partial, self.rect))

    def test_poly_in_rect_outside(self):
        "fails with every point outside"
        self.assertFalse( rects.poly_in_rect(self.poly_outside, self.rect), "%r should be inside %r" % (self.poly_outside, self.rect))



@test_for("rects.surround_poly")
class SurroundPolyTest(unittest.TestCase):
    def setUp(self):
        self.poly = [ (3,-1), (3,2), (4,5), (2,6), (1,5), (1, 2) ]
        self.rect = Rect(1,-1,4,8)

    def test_surround_rect(self):
        "same dimensions as expected rect"
        result = rects.surround_poly(self.poly)
        self.assertEquals(self.rect.x, result.x, "incorrect x (topleft)")
        self.assertEquals(self.rect.y, result.y, "incorrect y (topleft)")
        self.assertEquals(self.rect.width, result.width, "incorrect width")
        self.assertEquals(self.rect.height, result.height, "incorrect height")

    pass

if __name__ == "__main__":
    unittest.main()
