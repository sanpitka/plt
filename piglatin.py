
import string

from error import PigLatinError

class PigLatin:
    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        if not self.phrase:
            return "nil"
        return self.phrase

    def translate(self) -> str:
        words = self.phrase.split()
        translated_words = []
        vowels = "aeiouAEIOU"
        for word in words:
            if word.isupper():
                translated_words.append(self.translate_word(word, vowels).upper())
            elif word[0].isupper():
                translated_word = self.translate_word(word.lower(), vowels)
                translated_words.append(translated_word.capitalize())
            elif any(char.isupper() for char in word):
                raise PigLatinError("Invalid case: mixed case words are not allowed.")
            elif '-' in word:
                subwords = word.split('-')
                translated_subwords = [self.translate_word(subword, vowels) for subword in subwords]
                translated_words.append('-'.join(translated_subwords))
            elif any(char in string.punctuation for char in word):
                subword = ''.join([char for char in word if char not in string.punctuation])
                punctuation = ''.join([char for char in word if char in string.punctuation])
                translated_words.append(self.translate_word(subword, vowels) + punctuation)
            else:
                translated_words.append(self.translate_word(word, vowels))
        return " ".join(translated_words)

    def translate_word(self, word, vowels):
        if word[0] in vowels:
            if word[-1] == 'y':
                return word + "nay"
            elif word[-1] in vowels:
                return word + "yay"
            else:
                return word + "ay"
        else:
            first_vowel_idx = next((i for i, letter in enumerate(word) if letter in vowels), None)
            if first_vowel_idx is not None:
                return word[first_vowel_idx:] + word[:first_vowel_idx] + "ay"
            else:
                return word + "ay"

