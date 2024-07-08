class Anagram:
    def __init__(self, word) -> None:
        self._word = word
        self.anagrams = []

    @property
    def word(self):
        return self._word

    def match(self, words):
        original_sorted = sorted(self._word)
        for word in words:
            if sorted(word) == original_sorted:
                self.anagrams.append(word)
        return self.anagrams

