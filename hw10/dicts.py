#!/usr/bin/env python
"""
dicts.py

Dictionaries
============================================================ 
In this section, write some functions which build and 
manipulate python dictionaries.
"""

# 1. freq
#      Return a dictionary of the number of times each value
#      is in data.
#          >>> freq([ 1, 2, 2, 2, 2, 3, 4, 5, 1, 4, 1, 9, 10 ])
#          { 1: 3, 2: 4, 3: 1, 4: 1, 5: 1, 9: 1, 10: 1}

def freq(data):
    "calculate the frequency for each value in data"



# 2. Movie Reviews
#      Write two functions to help with scoring a movie.
#
#      score:
#        stores a score in the "movies" dictionary
#
#      avg_score:
#        returns the average score of a movie
#
#      Examples:
#      >>> score("Fargo", 4)
#      >>> score("Fargo", 5)
#      >>> score("Fargo", 5)
#      >>> avg_score("Fargo")
#      4.6666666667
#      >>> avg_score("missing movie")
#      None

movies = {}

def score(title, value):
    "register the score for a given movie out of 5"


def avg_score(title):
    "return the average score for a given movie"



# 3. parse_csv (Advanced)
#        Takes an input string and spits back a list of comma
#        separated values (csv) entries.  Hint, check the zip
#        and dict functions.
#
#        The point of this is to create your own parser, not to
#        use pythons builtin 'csv' library.
#
#           >>> csv = """
#           name,age,email
#           Foo, 24, foo@example.com
#           Bar ,22 ,bar@example.com
#           Baz, 20 , baz@gmail.com
#           """
#           >>> parse_csv(csv)
#           [ { "name": "Foo", "age": "24", "email": "foo@example.com" },
#             { "name": "Bar", "age": "22", "email": "bar@example.com" },
#             { "name": "Baz", "age": "20", "email": "baz@example.com" } ]            

def parse_csv(data):
    "parses a csv file into a list of dictionaries"

