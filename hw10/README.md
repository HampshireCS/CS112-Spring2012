Homework 10
=========================================
Matricies, Dictionaries, and Rects
-----------------------------------------

Welcome to another Thursday homework, this time about some of pythons larger datatypes.  Once again, complete all the functions defined in the following files:

 * `rects.py`
 * `multidim.py`
 * `dicts.py`

### Running the Tests

It seems the way the tests worked last week was a bit complicated so I've tried to simplify things.  First of all, the output is simpler, and there will be no tricky "you forgot to check for whether or not I was giving you numbers."

Here's how to run the tests:

```bash

# to run all the tests
$ python run_tests.py

# to run a specific file
$ python run_tests.py rects.py

# ...or
$ python run_tests.py rects

# to run a specific function
$ python run_tests.py dicts.freq

# to run multiple specific things
$ python run_tests.py rects dicts.freq

# to skip a specific file
$ python run_tests.py -multidim

# to skip a specific function
$ python run_tests.py -multidim.distance_from_player
```

Hopefully this will be easier to use.  That said, I'm looking for feedback on these testing things.  As you get used to them, let me know where you're having trouble with them in the homework and I'll try to fix it for the next time/next year.

## Advanced

In addition to the advanced questions, also fill in the functions for `users.py`.
