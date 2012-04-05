"""
util.py

"""

from pygame import Rect

def rel_rect(rect, parent):
    return Rect((rect.x - parent.x, rect.y - parent.y), rect.size)
