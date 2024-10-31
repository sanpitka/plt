class PigLatin:

    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        self.phrase = self.phrase.lower()
        return self.phrase

    def translate(self) -> str:
        pass
