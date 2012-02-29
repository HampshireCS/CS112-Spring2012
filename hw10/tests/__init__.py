from base import unittest

from test_dicts import *
from test_multidim import *
from test_rects import *
from test_users import *


def get_selected_tests(*args):
    tests = [ tc for tc in globals().values() if type(tc) is type and issubclass(tc, unittest.TestCase) ]

    tests = [ tc for tc in tests if hasattr(tc, "__testing__") ]

    args = list(args)
    for i,v in enumerate(args):
        if v.endswith(".py"):
            args[i] = v[:-3]

    pos = []
    neg = []
    for v in args:
        if v.startswith("-"):
            neg.append(v[1:])
        elif v.startswith("+"):
            pos.append(v[1:])
        else:
            pos.append(v)

    if pos:
        cases = []
        for p in pos:
            cases += [ tc for tc in tests if tc.__testing__.startswith(p) ]
    else:
        cases = tests

    for n in neg:
        cases = [ tc for tc in cases if not tc.__testing__.startswith(n) ]

    return cases

