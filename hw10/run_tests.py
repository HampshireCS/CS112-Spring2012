#!/usr/bin/env python

if __name__ == "__main__":
    import tests
    from tests.base import unittest

    import sys

    cases = tests.get_selected_tests(*sys.argv[1:])

    alltests = unittest.TestSuite([ unittest.TestLoader().loadTestsFromTestCase(case) for case in cases ])

    unittest.TextTestRunner().run(alltests)
