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
        self.assertIsInstance(self.rect, Shape, "Rectangles should be Shapes")

    def test_area(self):
        self.assertEqual(self.rect.area(), 8, "Area for Rect 2x4 should be 8")

    def test_perimeter(self):
        self.assertEqual(self.rect.perimeter(), 12, "Perimeter for Rect 2x4 should be 12")

@unittest.skipIf(not hasattr(shapes, "Square"), "No Square class defined")
class SquareTest(unittest.TestCase):
    def setUp(self):
        self.sq = Square(2)

    def test_is_shape(self):
        self.assertIsInstance(self.sq, Shape, "Squares should be Shapes")

    def test_is_rect(self):
        self.assertIsInstance(self.sq, Rect, "Squares should be Rects")

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
        self.assertIsInstance(self.circ, Shape, "Circles should be Shapes")

    def test_area(self):
        self.assertEqual(self.circ.area(), self.area, "Wrong area for Circle with radius 4")

    def test_perimeter(self):
        self.assertEqual(self.circ.perimeter(), self.perim, "Wrong perimeter for Circle with radius 4")


@unittest.skipIf(not hasattr(shapes, "Polygon"), "No Polygone class defined")
class PolygonTest(unittest.TestCase):
    def setUp(self):
        pts1 = (0,0), (1,0), (0,1)
        pts2 = (0,0), (1,0), (1,1), (0,1)
        pts3 = (0,0), (1,0), (2,0), (1,1), (0,1)
        self.poly1 = Polygon(*pts1)
        self.poly2 = Polygon(*pts2)
        self.poly3 = Polygon(*pts3)

        self.poly1_area = 0.5
        self.poly1_perim = 3.4142135623730951
        self.poly2_area = 1
        self.poly2_perim = 4
        self.poly3_area = 1.5
        self.poly3_perim = 5.4142135623730951

        self.poly1_str = "Polygon(" + ", ".join(map(repr, pts1)) + ")"
        self.poly2_str = "Polygon(" + ", ".join(map(repr, pts2)) + ")"
        self.poly3_str = "Polygon(" + ", ".join(map(repr, pts3)) + ")"

    def test_is_shape(self):
        self.assertIsInstance(self.poly1, Shape, "Polygons should be Shapes")

    def test_perimeter(self):
        self.assertEqual(self.poly1.perimeter(), self.poly1_perim, "Incorrect perimeter for %s" % self.poly1_str)
        self.assertEqual(self.poly2.perimeter(), self.poly2_perim, "Incorrect perimeter for %s" % self.poly2_str)
        self.assertEqual(self.poly3.perimeter(), self.poly3_perim, "Incorrect perimeter for %s" % self.poly3_str)

    def test_area(self):
        self.assertAlmostEqual(self.poly1.area(), self.poly1_area, msg="Incorrect area for %s" % self.poly1_str)
        self.assertAlmostEqual(self.poly2.area(), self.poly2_area, msg="Incorrect area for %s" % self.poly2_str)
        self.assertAlmostEqual(self.poly3.area(), self.poly3_area, msg="Incorrect area for %s" % self.poly3_str)

@unittest.skipIf(not hasattr(shapes, "Shape"), "No Shape class defined")
@unittest.skipIf(not hasattr(shapes, "Rect"), "No Rect class defined")
@unittest.skipIf(not hasattr(shapes, "Square"), "No Square class defined")
@unittest.skipIf(not hasattr(shapes, "Circle"), "No Circle class defined")
class HierarchyTest(unittest.TestCase):
    def setUp(self):
        self.circ = Circle(4)
        self.rect = Rect(4,4)
        self.sq = Square(4)
    
    def test_circle(self):
        self.assertIsInstance(self.circ, Shape, "Circle should be a Shape")
        self.assertNotIsInstance(self.circ, Rect, "Circle should not be a Rect")
        self.assertNotIsInstance(self.circ, Square, "Circle should not be a Square")
    def test_rect(self):
        self.assertIsInstance(self.rect, Shape, "Rect should be a Shape")
        self.assertNotIsInstance(self.rect, Circle, "Rect should not be a Circle")
        self.assertNotIsInstance(self.rect, Square, "Rect should not be a Square")
    def test_square(self):
        self.assertIsInstance(self.sq, Shape, "Square should be a Shape")
        self.assertIsInstance(self.sq, Rect, "Square should be a Rect")
        self.assertNotIsInstance(self.sq, Circle, "Square should not be a Circle")

@unittest.skipIf(not hasattr(shapes, "Shape"), "No Shape class defined")
@unittest.skipIf(not hasattr(shapes, "Rect"), "No Rect class defined")
@unittest.skipIf(not hasattr(shapes, "Square"), "No Square class defined")
@unittest.skipIf(not hasattr(shapes, "Circle"), "No Circle class defined")
@unittest.skipIf(not hasattr(shapes, "Polygon"), "No Polygon class defined")
class AdvHierarchyTest(unittest.TestCase):
    def test_poly(self):
        poly = Polygon((0,0), (1,0), (0,1))
        self.assertIsInstance(poly, Shape, "Polygon should be a Shape")
        self.assertNotIsInstance(poly, Rect, "Polygon should not be a Rect")
        self.assertNotIsInstance(poly, Square, "Polygon should not be a Square")
        self.assertNotIsInstance(poly, Circle, "Polygon should not be a Circle")

if __name__ == "__main__":
    unittest.main(verbosity=2)
