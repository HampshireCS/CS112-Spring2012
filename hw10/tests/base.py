import os
import sys

root_path = os.path.join(os.path.dirname(__file__), "..")
sys.path.insert(0, root_path)
import inspect

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

_modules = {}

def test_for(inp):
    mod,fn = inp.split('.')

    # module
    if not mod in _modules:
        try:
            _modules[mod] = __import__(mod)
        except ImportError:
            return unittest.skip("No such module '%s'" % mod)

    # function
    f = getattr(_modules[mod], fn, None)
    if f is None:
        return unittest.skip("No such method '%s.%s'" % (mod,fn))

    # make sure function is implemented
    if not_implemented(f):
        return unittest.skip("'%s.%s' is not implemented" % (mod,fn))

    # return testcase if everything works 
    def deco(cls):
        module = sys.modules[cls.__module__]
        setattr(module, mod, _modules[mod])
        cls.__testing__ = inp
        return cls
    return deco 


def not_implemented(fn):
    if fn is None:
        return False

    source = inspect.getsource(fn).strip()
    source = source.split(":",1)[1].strip()

    if source[0:3] == '"""':
        source = source[3:]
        end = source.find('"""')
        source = source[end+3:].strip().splitlines()
    elif source[0:3] == "'''":
        source = source[3:]
        end = source.find("'''")
        source = source[end+3:].strip().splitlines()
    elif source[0] == "'" or source[0] == '"':
        source = source.splitlines()[1:]
    else:
        source = source.splitlines()

    if len(source) > 1:
        return False
    elif len(source) == 1 and source[0].strip() != "pass":
        return False

    return True



