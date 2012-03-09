#!/usr/bin/env python

import math

try:
    import unittest2 as unittest
except:
    import unittest

import shapes
from shapes import *

@unittest.skipIf(not hasattr(shapes, "Shape"), "No Shape class defined")
class ShapeTest(unittest.TestCase):

    def test_shape_does_nothing(self):
        shape = Shape()
        self.assertTrue(hasattr(Shape, "area"), "Shape should have an abstract area function")
        self.assertTrue(hasattr(Shape, "perimeter"), "Shape should have an abstract perimeter function")
        self.assertIsNone(shape.area(), "Abstract Shape should have no area")
        self.assertIsNone(shape.perimeter(), "Abstract Shape should have no perimeter")


@unittest.skipIf(not hasattr(shapes, "Rect"), "No Rect class defined")
class RectTest(unittest.TestCase):
    def setUp(self):
        self.rect = Rect(2,4)

    def test_is_shape(self):
        self.assertTrue(isinstance(self.rect, Shape), "Rectangles should be Shapes")

    def test_area(self):
        self.assertEqual(self.rect.area(), 8, "Area for Rect 2x4 should be 8")

    def test_perimeter(self):
        self.assertEqual(self.rect.perimeter(), 12, "Perimeter for Rect 2x4 should be 12")

@unittest.skipIf(not hasattr(shapes, "Square"), "No Square class defined")
class SquareTest(unittest.TestCase):
    def setUp(self):
        self.sq = Square(2)

    def test_is_shape(self):
        self.assertTrue(isinstance(self.sq, Shape), "Squares should be Shapes")

    def test_is_rect(self):
        self.assertTrue(isinstance(self.sq, Rect), "Squares should be Rectangles")

    def test_rect_methods(self):
        self.assertEqual(Rect.area, Square.area, "Squares should have the same area method as Rectangles")
        self.assertEqual(Rect.perimeter, Square.perimeter, "Squares should have the same perimeter method as Rectangles")

    def test_area(self):
        self.assertEqual(self.sq.area(), 4, "Area for Square 2x2 should be 4")

    def test_perimeter(self):
        self.assertEqual(self.sq.perimeter(), 8, "Perimeter for Square 2x2 should be 8")

@unittest.skipIf(not hasattr(shapes, "Circle"), "No Circle class defined")
class CircleTest(unittest.TestCase):
    def setUp(self):
        self.circ = Circle(4)
        self.area = 16 * math.pi
        self.perim = 8 * math.pi

    def test_is_shape(self):
        self.assertTrue(isinstance(self.circ, Shape), "Circles should be Shapes")

    def test_area(self):
        self.assertEqual(self.circ.area(), self.area, "Wrong area for Circle with radius 4")

    def test_perimeter(self):
        self.assertEqual(self.circ.perimeter(), self.perim, "Wrong perimeter for Circle with radius 4")
if __name__ == "__main__":
    unittest.main(verbosity=2)
