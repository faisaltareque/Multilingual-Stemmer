from snowballstemmer import TamilStemmer as TS

class TamilStemmer(TS):
    def __init__(self):
        super().__init__()

    def stem(self, word):
        return super().stemWord(word)
    
