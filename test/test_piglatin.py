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

    def test_translate_word_starting_with_vowel_1(self):
        piglatin = PigLatin("any")
        translation = piglatin.translate()
        self.assertEqual("anynay", translation)

    def test_translate_word_starting_with_vowel_2(self):
        piglatin = PigLatin("apple")
        translation = piglatin.translate()
        self.assertEqual("appleyay", translation)

    def test_translate_word_starting_with_vowel_3(self):
        piglatin = PigLatin("ask")
        translation = piglatin.translate()
        self.assertEqual("askay", translation)

