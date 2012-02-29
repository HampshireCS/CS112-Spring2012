#!/usr/bin/env python

from base import unittest, not_implemented, test_for

from pygame import Rect

@test_for("dicts.freq")
class FreqTest(unittest.TestCase):
    def setUp(self):
        self.string = "aaaabbbaaddaacceedxddff"
        self.string_freq = { "a": 8, "b": 3, "c": 2, "d": 5, "e":2, "f": 2, "x": 1 }

        self.array = [1,1,2,5,4,3,6,7,4,2,7,3,2,1,6,1]
        self.array_freq = { 7:2, 1: 4, 2: 3, 5: 1, 4: 2, 3: 2, 6: 2 }

    def test_freq_type(self):
        "returns a dict"
        self.assertIsInstance( dicts.freq([]), dict)

    def test_freq_empty(self):
        "handles empty lists"
        self.assertEquals( dicts.freq([]), dict())

    def test_freq_array(self):
        "handles arrays"
        self.assertDictEqual( dicts.freq(self.array), self.array_freq)

    def test_freq_string(self):
        "handles strings"
        self.assertDictEqual( dicts.freq(self.string), self.string_freq)



@test_for("dicts.score")
class MovieScoreTest(unittest.TestCase):
    def test_score_return(self):
        "score returns nothing"
        self.assertIsNone( dicts.score("Something", 3) )

    def test_score_modifies(self):
        "score modifies movies"
        self.assertIsNone( dicts.movies.get("Mod") )
        dicts.score("Mod", 3)
        self.assertIsNotNone( dicts.movies.get("Mod") )



@test_for("dicts.score")
@test_for("dicts.avg_score")
class MovieAvgScoreTest(unittest.TestCase):
    def test_avg_score_missing(self):
        "avg_score for missing movie"
        self.assertIsNone( dicts.avg_score("Missing") )

    def assertScore(self, expected, title, *vals):
        for v in vals:
            dicts.score(title, v)

        result = dicts.avg_score(title)
        movie = dicts.movies.get(title)
        self.assertEquals( result, expected, "Incorrect average.\nValue of movies[%r]: %r" % (title, movie))


    def test_avg_score_single(self):
        "avg_score calculated"

        self.assertScore(3, "Foo", 3)
        self.assertScore(4, "Bar", 3, 5)
        self.assertScore(4.5, "Baz", 4, 5)
        self.assertScore(14/3.0, "Movie", 4, 5, 5)


@test_for("dicts.parse_csv")
class ParseCSVTest(unittest.TestCase):
    def setUp(self):
        self.csv = """
            id , name, school , concentration
            24, Jeff, Hampshire, CS
            67 ,  Alonzo , UMass  , NS
            100, Cindy, Hampshire, NS
            101 , Debra , Amherst , CSI
        """

        self.parsed = [
            { "id": "24", "name": "Jeff", "school": "Hampshire", "concentration": "CS" },
            { "id": "67", "name": "Alonzo", "school": "UMass", "concentration": "NS" },
            { "id": "100", "name": "Cindy", "school": "Hampshire", "concentration": "NS" },
            { "id": "101", "name": "Debra", "school": "Amherst", "concentration": "CSI" },
        ]

    def test_parse_csv_entries(self):
        "correct number of entries"
        result = dicts.parse_csv(self.csv)
        self.assertEquals(len(result), 4, "expected 4 entries")

    def test_parse_csv_keys(self):
        "entries have correct keys"
        result = dicts.parse_csv(self.csv)

        parsed_keys = self.parsed[0].keys()
        result_keys = result[0].keys()
        
        self.assertSetEqual( set(parsed_keys), set(result_keys), "keys don't match")
        
    def test_parse_csv(self):
        "get correct results"
        result = dicts.parse_csv(self.csv)
        for expected, entry in zip(self.parsed, result):
            self.assertDictEqual( expected, entry, "entry doesn't match")

if __name__ == "__main__":
    unittest.main()
