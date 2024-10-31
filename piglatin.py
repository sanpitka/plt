
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
            if word[0] in vowels:
                if word[-1] == 'y':
                    translated_word = word + "nay"
                elif word[-1] in vowels:
                    translated_word = word + "yay"
                else:
                    translated_word = word + "ay"
            else:
                first_vowel_idx = next((i for i, letter in enumerate(word) if letter in vowels), None)
                if first_vowel_idx is not None:
                    translated_word = word[first_vowel_idx:] + word[:first_vowel_idx] + "ay"
                else:
                    translated_word = word + "ay"
            translated_words.append(translated_word)
        return " ".join(translated_words)

