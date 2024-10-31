
class PigLatin:

    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        if not self.phrase:
            return "nil"
        self.phrase = self.phrase.lower()
        return self.phrase

    def translate(self) -> str:
        pass

