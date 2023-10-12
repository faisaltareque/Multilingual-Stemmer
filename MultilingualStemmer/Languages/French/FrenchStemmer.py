from snowballstemmer import FrenchStemmer as FS

class FrenchStemmer(FS):
    def __init__(self):
        super().__init__()

    def stem(self, word):
        return super().stemWord(word)
    
