from triggers import Trigger

class OnExactPhrase(Trigger):

    def __init__(self, phrase, macro):
        super().__init__(macro)
        self.phrase = phrase

    def check(self, text):
        return text == self.phrase

class OnPhraseContained(Trigger):

    def __init__(self, phrase, macro):
        super().__init__(macro)
        self.phrase = phrase

    def check(self, text):
        return text.contains(self.phrase)

class OnVolumeRange(Trigger):
    def __init__(self, rng, macro):
        super().__init__(macro)
        self.a, self.b = rng

    def check(self, volume):
        return self.a <= volume <= self.b