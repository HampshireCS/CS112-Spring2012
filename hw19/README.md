Homework 19
=========================
Recursion and QuadTrees
-------------------------

In this assignment, you will be fleshing out a [Quadtree](http://en.wikipedia.org/wiki/Quadtree).  Quadtrees are traditionally used in graphics programming to quickly eliminate large groups of points.

QuadTreeNode is already mostly a quadtree.  However, in order to actually use it in a program, there should be easier ways to access the data inside the QuadTree.  Specifically, we need a way to get a list of all the points in the quadtree and a way to get every rectangle (quadrents).

As you add the methods in this homework, run `test_quad.py` to run the normal battery of unit tests to see if it works.  Once you are completely done, you can use `./rundemo` to run a graphical demo to see your quadtree in action.

> `rundemo` is a python file so can just be opened in IDLE on Windows.


Getting the Points (get_points)
--------------------------------

Add a method `get_points` to QuadTreeNode.  This method will fetch a list of every point stored in a QuadTreeNode and it's children.  Since each 

**Requirements:**

 * if there are no points, return an empty list
 * if there is only one point, return a list with only that point in it
 * if there is more than one point, return a list with every point
 * the order the points are output doesn't matter

**Example:**

```python
>>> qtree = QuadTreeNode(Rect(0, 0, 100, 100))
>>> # no points
>>> qtree.get_points()
[]
>>> # one point
>>> qtree.add_point((25, 25))
>>> qtree.get_points()
[ (25,25) ]
>>> # many points
>>> qtree.add_point((75, 75))
>>> qtree.add_point((22, 22))
[ (25,25), (75, 75), (22, 22) ]
```



Getting Rects (quadrents)
--------------------------------

Add a method `get_rects` which fetches every rectangle out of a QuadTree.  This includes the root node and its children if it has any and so on.  This should be a flat list of rectangles (not lists in lists).

**Requirements:**

 * if there are zero/one points, return just the root rect
 * if there is more than one point, return the root rect and all it's children
 * if there is more than one level of nesting, return nested child.
 * order of rects doesn't matter

> **HINT:** You can use an optional `rects` parameter to keep track of all the rects as you add them.  Since arrays are a reference, adding a rect to an array as you recurse is a good way to track all the values

**Example:**

```python
>>> qtree = QuadTreeNode(Rect(0, 0, 100, 100))
>>> # no points
>>> qtree.get_rects()
[<rect(0, 0, 100, 100)>]
>>> # one point
>>> qtree.add_point((10, 10))
>>> qtree.get_rects()
[<rect(0, 0, 100, 100)>]
>>> # two points in different quadrents
>>> qtree.add_point((75, 75))
>>> qtree.get_rects()
[<rect(0, 0, 100, 100)>, <rect(0, 0, 50, 50)>, <rect(50, 0, 50, 50)>, <rect(0, 50, 50, 50)>, <rect(50, 50, 50, 50)>]
>>> # two points in the same quadrent
>>> qtree.add_point((40, 40))
>>> qtree.get_rects()
[<rect(0, 0, 100, 100)>, <rect(0, 0, 50, 50)>, <rect(0, 0, 25, 25)>, <rect(25, 0, 25, 25)>, <rect(0, 25, 25, 25)>, <rect(25, 25, 25, 25)>, <rect(25, 0, 25, 25)>, <rect(0, 25, 25, 25)>, <rect(25, 25, 25, 25)>]
```

[Advanced] Collide Point with QuadTree (collidepoint)
--------------------------------------------------------

Add a method `collidepoint` which returns the smallest QuadTreeNode which collides with a given point.

**Requirements:**
 * if the point is not within the QuadTreeNode, return None
 * if the QuadTreeNode is not split and the point collides, return itself
 * if the QuadTreeNode is split, return collidepoint for the child

