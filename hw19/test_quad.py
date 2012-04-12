#!/usr/bin/env python

import math

from pygame import Rect

try:
    import unittest2 as unittest
except:
    import unittest

from quad import QuadTreeNode

class QuadTreeTest(unittest.TestCase):

    def setUp(self):
        self.qtree = QuadTreeNode(Rect(0,0,100, 100))

    # get_points tests
    @unittest.skipIf(not hasattr(QuadTreeNode, "get_points"), "missing get_points")
    def test_get_points_empty(self):
        "if no points have been added, get_points should return an empty list"
        self.assertItemsEqual(self.qtree.get_points(), [], "No points have been added to the quadtree, should return an empty list")

    @unittest.skipIf(not hasattr(QuadTreeNode, "get_points"), "missing get_points")
    def test_get_points_one(self):
        "if only one point is added, a list containing that one point should be returned"
        self.qtree.add_point((25, 25))
        self.assertItemsEqual(self.qtree.get_points(), [(25,25)], "One point has been added, only one point should be returned")

    @unittest.skipIf(not hasattr(QuadTreeNode, "get_points"), "missing get_points")
    def test_get_points_many(self):
        "get_points should return all points added"

        self.qtree.add_point((25, 25))
        self.qtree.add_point((75, 75))
        self.qtree.add_point((22, 22))
        self.assertItemsEqual(self.qtree.get_points(), [(22,22), (75,75), (25,25)], "Incorrect points returned")

    # get_rects tests
    @unittest.skipIf(not hasattr(QuadTreeNode, "get_rects"), "missing get_rects")
    def test_get_rects_simple(self):
        "if zero or one points have been added, get_rects should just return a list with the root's rect"
        self.assertIn(self.qtree.rect, self.qtree.get_rects(), "root rect missing, no points")
        self.assertEqual(1, len(self.qtree.get_rects()), "too many rects returned, no points")
        
        self.qtree.add_point((30,30))
        self.assertIn(self.qtree.rect, self.qtree.get_rects(), "root rect missing, one point")
        self.assertEqual(1, len(self.qtree.get_rects()), "too many rects returned, one point")
    
    @unittest.skipIf(not hasattr(QuadTreeNode, "get_rects"), "missing get_rects")
    def test_get_rects_split(self):
        "if only one split has happened, the root and it's children should be returned"

        self.qtree.add_point((25,25))
        self.qtree.add_point((75,75))
        rects = self.qtree.get_rects()

        self.assertEqual(5, len(rects), "expected 5 rects (root and children)")
        self.assertIn(self.qtree.rect, rects, "root rect missing")
        self.assertIn(self.qtree.nw.rect, rects, "root.nw rect missing")
        self.assertIn(self.qtree.ne.rect, rects, "root.ne rect missing")
        self.assertIn(self.qtree.sw.rect, rects, "root.sw rect missing")
        self.assertIn(self.qtree.se.rect, rects, "root.se rect missing")

    @unittest.skipIf(not hasattr(QuadTreeNode, "get_rects"), "missing get_rects")
    def test_get_rects_complex(self):
        "if many splits have occured, all rects should be returned"

        self.qtree.add_point((10,10))
        self.qtree.add_point((40,40))
        self.qtree.add_point((75,75))
        rects = self.qtree.get_rects()

        self.assertEqual(9, len(rects), "expected 5 rects (root and children)")
        self.assertIn(self.qtree.rect, rects, "root rect missing")
        self.assertIn(self.qtree.nw.rect, rects, "root.nw rect missing")
        self.assertIn(self.qtree.ne.rect, rects, "root.ne rect missing")
        self.assertIn(self.qtree.sw.rect, rects, "root.sw rect missing")
        self.assertIn(self.qtree.se.rect, rects, "root.se rect missing")
        self.assertIn(self.qtree.nw.nw.rect, rects, "root.nw.nw rect missing")
        self.assertIn(self.qtree.nw.ne.rect, rects, "root.nw.ne rect missing")
        self.assertIn(self.qtree.nw.sw.rect, rects, "root.nw.sw rect missing")
        self.assertIn(self.qtree.nw.se.rect, rects, "root.nw.se rect missing")


    # collidepoint tests
    @unittest.skipIf(not hasattr(QuadTreeNode, "collidepoint"), "missing collidepoints")
    def test_collidepoint_out_of_bounds(self):
        "if point is out of bounds, collidepoint should return None"
        self.assertIsNone(self.qtree.collidepoint((101,101)), "point is out of bounds, should return None")

    @unittest.skipIf(not hasattr(QuadTreeNode, "collidepoint"), "missing collidepoints")
    def test_collidepoint_simple(self):
        "if there are zero or one points, collidepoint just needs to return the node"
        self.assertEqual(self.qtree, self.qtree.collidepoint((50,50)), "no points, expected root node")
        self.qtree.add_point((50,50))
        self.assertEqual(self.qtree, self.qtree.collidepoint((50,50)), "one points, expected root node")


    @unittest.skipIf(not hasattr(QuadTreeNode, "collidepoint"), "missing collidepoints")
    def test_collidepoint_split(self):
        "if there is one split, collidepoint needs to return the correct quadrent"
        self.qtree.add_point((75,75))
        self.qtree.add_point((25,25))

        self.assertEqual(self.qtree.nw, self.qtree.collidepoint((25,25)), "expected nw")
        self.assertEqual(self.qtree.ne, self.qtree.collidepoint((75,25)), "expected ne")
        self.assertEqual(self.qtree.sw, self.qtree.collidepoint((25,75)), "expected sw")
        self.assertEqual(self.qtree.se, self.qtree.collidepoint((75,75)), "expected se")
        
    @unittest.skipIf(not hasattr(QuadTreeNode, "collidepoint"), "missing collidepoints")
    def test_collidepoint_complex(self):
        "if there is one split, collidepoint needs to return the correct quadrent"
        self.qtree.add_point((75,75))
        self.qtree.add_point((10,10))
        self.qtree.add_point((40,40))

        self.assertEqual(self.qtree.ne, self.qtree.collidepoint((75,25)), "expected ne")
        self.assertEqual(self.qtree.sw, self.qtree.collidepoint((25,75)), "expected sw")
        self.assertEqual(self.qtree.se, self.qtree.collidepoint((75,75)), "expected se")

        self.assertEqual(self.qtree.nw.nw, self.qtree.collidepoint((10,10)), "expected nw.nw")
        self.assertEqual(self.qtree.nw.ne, self.qtree.collidepoint((40,10)), "expected nw.ne")
        self.assertEqual(self.qtree.nw.sw, self.qtree.collidepoint((10,40)), "expected nw.sw")
        self.assertEqual(self.qtree.nw.se, self.qtree.collidepoint((40,40)), "expected nw.se")

if __name__ == "__main__":
    unittest.main()
