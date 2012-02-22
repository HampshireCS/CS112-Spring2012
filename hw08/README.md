===================
Homework 8
===================
Functions
-------------------

Go into the following files and implement the functions as they are described.

 * `basic_funcs.py` - a simple greeter and drawing a box
 * `math_funcs.py` - simple math equations
 * `collision_funcs.py` - check if a point is in a box

There are rough descriptions on how to implement each function.  The way you know it is working
100% correctly is with unit testing.

> Unit testings is a way programmers have to write a bunch of test cases for things like functions
> and test to make sure they are working.  I have written a bunch of test cases for you.

To test your functions, run `python hw08.py` to run all the tests.  It will tell who what isn't implemented, what's working, and what is broken.  When you are done with your homework, the result should look something like this.

```
$ python hw08.py
----------------------------------------
test_greeter_basic (__main__.GreeterTest) ... ok
test_greeter_case (__main__.GreeterTest) ... ok
test_greeter_int (__main__.GreeterTest) ... ok
test_box (__main__.BoxTest) ... ok
test_box_error_too_small (__main__.BoxTest) ... ok
test_box_error_type (__main__.BoxTest) ... ok
test_tree (__main__.TreeTest) ... ok
test_distance (__main__.DistanceTest) ... ok
test_normalize_many (__main__.NormalizeTest) ... ok
test_normalize_two (__main__.NormalizeTest) ... ok
test_normalize_zeros (__main__.NormalizeTest) ... ok
test_point_in_box (__main__.PointInBoxTest) ... ok
test_point_in_box_edges (__main__.PointInBoxTest) ... ok

----------------------------------------------------------------------
Ran 13 tests in 0.001s

OK
```

## Advanced

As usual, implement the advanced only portions of the basic homework.  In addition to this, program `adv_nims.py`.  I have laid out all the functions you should need and the main game loop.  Run `python adv_nims_tests.py` to see which pieces you have left to program and what still doesn't work.  Once the tests run without error, your game should just work.

> This is known as test driven development, where you start with your test cases and keep modifying your functions/code until everything works without error.  This is good for complicated code so you know which parts of your code work and which don't.
