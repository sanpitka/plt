import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_input_phrase(self):
        piglatin = PigLatin("hello world")
        phrase = piglatin.get_phrase()
        self.assertEqual("hello world", phrase)

    def test_null_phrase(self):
        piglatin = PigLatin("")
        phrase = piglatin.get_phrase()
        self.assertEqual("nil", phrase)

