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

    def test_translate_word_starting_with_single_consonant(self):
        piglatin = PigLatin("hello")
        translation = piglatin.translate()
        self.assertEqual("ellohay", translation)

    def test_translate_word_starting_with_more_consonants(self):
        piglatin = PigLatin("known")
        translation = piglatin.translate()
        self.assertEqual("ownknay", translation)

    def test_translate_phrase_1(self):
        piglatin = PigLatin("hello world")
        translation = piglatin.translate()
        self.assertEqual("ellohay orldway", translation)

    def test_translate_phrase_2(self):
        piglatin = PigLatin("well-being")
        translation = piglatin.translate()
        self.assertEqual("ellway-eingbay", translation)

    def test_translate_phrase_containing_punctuations(self):
        piglatin = PigLatin("hello world!")
        translation = piglatin.translate()
        self.assertEqual("ellohay orldway!", translation)


