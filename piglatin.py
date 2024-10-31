
class PigLatin:
    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        if not self.phrase:
            return "nil"
        return self.phrase.lower()

    def translate(self) -> str:
        words = self.phrase.lower().split()
        translated_words = []
        vowels = "aeiou"
        for word in words:
            if '-' in word:
                subwords = word.split('-')
                translated_subwords = [self.translate_word(subword, vowels) for subword in subwords]
                translated_word = '-'.join(translated_subwords)
            else:
                translated_word = self.translate_word(word, vowels)
            translated_words.append(translated_word)
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

