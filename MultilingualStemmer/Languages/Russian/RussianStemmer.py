from snowballstemmer import RussianStemmer as RS

class RussianStemmer(RS):
    def __init__(self):
        super().__init__()

    def stem(self, word):
        return super().stemWord(word)
    
