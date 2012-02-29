#!/usr/bin/env python
import os
import pickle

from base import unittest, not_implemented, test_for

ROOT = os.path.dirname(__file__)
f = open( os.path.join(ROOT, "users.pkl"), "rb")
USERS = pickle.load(f)
f.close()

@test_for("users.followers")
class FollowersTest(unittest.TestCase):
    def setUp(self):
        self.theo = set(['Ralph'])
        self.zeek = set(['Xander', 'Max', 'Carol', 'Bob', 'Igor', 'Karl'])
        self.zeek_jansen = set(['Igor', 'Xander', 'Max', 'Frank', 'Carol', 'Bob', 'Karl'])

    def test_followers_basic(self):
        "one name"
        result = set(users.followers(USERS, "Theo"))
        self.assertSetEqual( self.theo, result)

        result = set(users.followers(USERS, "Zeek"))
        self.assertSetEqual(self.zeek, result)

    def test_followers_multiple(self):
        "multiple names"
        result = set(users.followers(USERS, "Zeek", "Jansen"))
        self.assertSetEqual(self.zeek_jansen, result)


@test_for("users.underage_follows")
class UnderageFollowsTest(unittest.TestCase):
    def setUp(self):
        self.answer = set(['Igor', 'Frank', 'Ned', 'Ralph', 'Alice', 'Yolanda', 'Uma', 'George', 'Wally', 'Opie', 'Everett'])

    def test_underage_follows(self):
        "got expected set"
        result = set(users.underage_follows(USERS))
        self.assertSetEqual(self.answer, result)

@test_for("users.foaf")
class FoafTest(unittest.TestCase):
    def setUp(self):
        self.carol = set(['Damien'])
        self.zeek = set(['Lola', 'Igor', 'Xander', 'Max', 'Everett', 'Ralph', 'Alice', 'Vera', 'Frank', 'Wally', 'Jansen', 'Paul', 'Opie', 'Sally', 'Ned', 'Karl'])

    def test_foaf_type(self):
        "foaf returns the correct type"
        result =users.foaf(USERS, "Sally")
        self.assertIsInstance(users.foaf(USERS, "Sally"), set)

    def test_foaf_exclude_self(self):
        "foaf doesn't include the user it is being run on"
        self.assertNotIn("Jansen", users.foaf(USERS, "Jansen"))


    def test_foaf_basic(self):
        "got expected sets"
        result = users.foaf(USERS, "Carol")
        self.assertSetEqual(self.carol, result)
        
        result = users.foaf(USERS, "Zeek")
        self.assertSetEqual(self.zeek, result)

@test_for("users.age_demographics")
class AgeDemographicsTest(unittest.TestCase):
    def setUp(self):
        self.answer = {8: 21.5, 9: 21.428571428571427, 11: 21.333333333333332, 13: 18.333333333333332, 14: 15.25, 16: 15.4, 18: 18.800000000000001, 19: 15.666666666666666, 20: 14.0, 22: 24.125, 24: 22.199999999999999, 27: 21.199999999999999, 28: 25.399999999999999, 30: 12.666666666666666, 31: 22.833333333333332}
        
    def test_age_demographics(self):
        "all values are correct"
        result = users.age_demographics(USERS)
        self.assertDictEqual(self.answer, result)

if __name__ == "__main__":
    unittest.main()
