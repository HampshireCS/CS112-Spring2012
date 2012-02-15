#!/usr/bin/env python

swears = [
    ['ass', 'butt'],
    ['fuck', 'fudge'],
    ['shit', 'poo'],
    ['piss', 'tinkle']
]


comment = raw_input("Leave a comment, just don't use any dirty words: ")

for bad, good in swears:
    comment = comment.replace(bad, good)

print "Your comment:"
print "\t", comment
