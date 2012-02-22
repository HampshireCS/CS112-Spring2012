import sys
import unittest
from StringIO import StringIO

from basic_funcs import *
from math_funcs import *
from collision_funcs import *

class StdOutTestCase(unittest.TestCase):
    def setUp(self):
        self.held = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = self.held

    def assertOutput(self, _, outp, msg=None):
        actual = sys.stdout.getvalue()   

        if sys.stdout.getvalue() != (outp + "\n"):
            if msg is None:
                actual = sys.stdout.getvalue()
                out = StringIO()
                out.write("\n")
                out.write("Expected:\n")
                out.writelines('\t%s\n'%s for s in outp.splitlines())
                out.write("Actual:\n")
                out.writelines('\t%s\n'%s for s in actual.splitlines())
                msg = out.getvalue()

            self.fail(msg)
        sys.stdout.truncate(0)


class GreeterTest(StdOutTestCase):
    def test_greeter_basic(self):
        self.assertOutput(greeter(""), "hello, ")
        self.assertOutput(greeter("world"), "hello, world")

    def test_greeter_int(self):
        self.assertOutput(greeter(2), "hello, 2")

    def test_greeter_case(self):
        self.assertOutput(greeter("DaViD"), "hello, david")

BOXES = {
    (1,1): "+",
    (2,1): "++",
    (3,2): "+-+\n+-+",
    (3,3): "+-+\n| |\n+-+",
    (7,5): "+-----+\n|     |\n|     |\n|     |\n+-----+"
}


class BoxTest(StdOutTestCase):
    error_msg = "Error: Invalid Dimensions"

    def test_box(self):
        for key,outp in BOXES.items():
            w,h = key
            self.assertOutput(box(w,h), outp)

    def test_box_error_too_small(self):
        self.assertOutput(box(0,0), self.error_msg)
        self.assertOutput(box(-13,3), self.error_msg)
        self.assertOutput(box(3,-3), self.error_msg)

    def test_box_error_type(self):
        self.assertOutput(box("", ""), self.error_msg)
        self.assertOutput(box(3.5, 3), self.error_msg)
        self.assertOutput(box(3, 3.5), self.error_msg)


# xmas tree

TREES = [
    (((), ()), '    *\n    ^\n   ^-^\n  ^-^-^\n ^-^-^-^\n^-^-^-^-^\n   | |\n   | |'),
    (((1,), ()), '*\n^\n|\n|'), 
    (((3,), ()), '  *\n  ^\n ^-^\n^-^-^\n  |\n  |'),
    (((1, 1), ()), '*\n^\n|'), 
    (((4, 1), ()), '   *\n   ^\n  ^-^\n ^-^-^\n^-^-^-^\n  | |'),
    (((5, 2), ()), '    *\n    ^\n   ^-^\n  ^-^-^\n ^-^-^-^\n^-^-^-^-^\n   | |\n   | |'),
    (((5,), (('star', '#'),)), '    #\n    ^\n   ^-^\n  ^-^-^\n ^-^-^-^\n^-^-^-^-^\n   | |\n   | |'),
    (((), (('star', '%'), ('ornament', '('), ('leaf', '!'))), '    %\n    !\n   !(!\n  !(!(!\n !(!(!(!\n!(!(!(!(!\n   | |\n   | |'), 
    (((5, 2, '@', '^', '&'), ()), '    &\n    ^\n   ^@^\n  ^@^@^\n ^@^@^@^\n^@^@^@^@^\n   | |\n   | |'),
    (((), (('star', None),)), '    ^\n   ^-^\n  ^-^-^\n ^-^-^-^\n^-^-^-^-^\n   | |\n   | |'),
    (((), (('ornament', None),)), '    *\n    ^\n   ^ ^\n  ^ ^ ^\n ^ ^ ^ ^\n^ ^ ^ ^ ^\n   | |\n   | |'),
    (((), (('leaf', None),)), '    *\n     \n    - \n   - - \n  - - - \n - - - - \n   | |\n   | |'),
]

class TreeTest(unittest.TestCase):
    def test_tree(self):
        for key, outp in TREES:
            args,kwargs = key
            
            result = tree(*args, **dict(kwargs))
            
            msg = "Error: tree("
            if args:
                msg += ", ".join(str(i) for i in args)
            if kwargs and args:
                msg += ", "
            if kwargs:
                msg += ", ".join("%s=%r" % item for item in kwargs)
            msg += ")"

            msg += "\n"
            msg += "Expected:\n"
            msg += outp
            msg += "\n"
            msg += "Actual:\n"
            msg += result

            self.assertEqual(result, outp, msg)

class DistanceTest(unittest.TestCase):
    def test_distance(self):
        self.assertEquals(distance((0,0), (4,3)), 5)
        self.assertEquals(distance((0,0), (0,0)), 0)
        self.assertEquals(distance((-4,-10), (4, 5)), 17)

class NormalizeTest(unittest.TestCase):
    def test_normalize_two(self):
        self.assertEquals(normalize((1,0)), [1.0,0.0])
        self.assertEquals(normalize((0,1)), [0.0,1.0])
        self.assertEquals(normalize((3,4)), [3/5.0, 4/5.0])

    def test_normalize_many(self):
        self.assertEquals(normalize((0,0,0,1)), [0.0,0.0,0.0,1.0])

        l = math.sqrt(86)
        self.assertEquals(normalize((3,4,5,6)), [3/l,4/l,5/l,6/l])

    def test_normalize_zeros(self):
        self.assertEquals(normalize((0,0)), (0,0), "handle zeros")
        self.assertEquals(normalize((0,0,0)), (0,0,0), "handle zeros")

class PointInBoxTest(unittest.TestCase):
    def test_point_in_box(self):
        box = (10,10,10,10)
        self.assertFalse(point_in_box((0,0), box))
        self.assertFalse(point_in_box((15,0), box))
        self.assertFalse(point_in_box((25,0), box))
        self.assertFalse(point_in_box((0,15), box))
        self.assertTrue(point_in_box((15,15), box))
        self.assertFalse(point_in_box((25,15), box))
        self.assertFalse(point_in_box((0,30), box))
        self.assertFalse(point_in_box((15,30), box))
        self.assertFalse(point_in_box((25,30), box))

    def test_point_in_box_edges(self):
        box = (10,10,10,10)
        self.assertTrue(point_in_box((10,10),box))
        self.assertTrue(point_in_box((10,15),box))
        self.assertTrue(point_in_box((15,10),box))
        self.assertFalse(point_in_box((20,20),box))
        self.assertFalse(point_in_box((20,15),box))
        self.assertFalse(point_in_box((15,20),box))


if __name__ == "__main__":
    suite = unittest.TestSuite()

    # basic
    if globals().get("greeter") is not None:
        tests = unittest.TestLoader().loadTestsFromTestCase(GreeterTest)
        suite.addTests(tests)
    else:
        print "'greeter' is not implemented"

    if globals().get("box") is not None:
        tests = unittest.TestLoader().loadTestsFromTestCase(BoxTest)
        suite.addTests(tests)
    else:
        print "'box' is not implemented"

    if globals().get("tree") is not None:
        tests = unittest.TestLoader().loadTestsFromTestCase(TreeTest)
        suite.addTests(tests)
    else:
        print "'tree' is not implemented"

    # math
    if globals().get("distance") is not None:
        tests = unittest.TestLoader().loadTestsFromTestCase(DistanceTest)
        suite.addTests(tests)
    else:
        print "'distance' is not implemented"

    if globals().get("normalize") is not None:
        tests = unittest.TestLoader().loadTestsFromTestCase(NormalizeTest)
        suite.addTests(tests)
    else:
        print "'normalize' is not implemented"

    # collision
    if globals().get("point_in_box") is not None:
        tests = unittest.TestLoader().loadTestsFromTestCase(PointInBoxTest)
        suite.addTests(tests)
    else:
        print "'point_in_box' is not implemented"
    
    print "-"*40
    unittest.TextTestRunner(verbosity=2).run(suite)
