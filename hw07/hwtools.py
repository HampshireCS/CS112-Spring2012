#!/usr/bin/env python
"""
hwtools.py

A bunch of functions needed to make the homeworks a bit easier.
"""

__ = "FILL_ME_IN"

def input_nums(msg="Enter some numbers, seperated by ',':  "):
    inp = raw_input(msg).strip()
    return [ int(c.strip()) for c in inp.split(",") ]

__all__ = ["__", "input_nums"]
