from snowballstemmer import SpanishStemmer as SS

class SpanishStemmer(SS):
    def __init__(self):
        super().__init__()

    def stem(self, word):
        return super().stemWord(word)
    
