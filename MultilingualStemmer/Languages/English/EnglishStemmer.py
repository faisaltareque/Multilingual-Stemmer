from snowballstemmer import EnglishStemmer as ES

class EnglishStemmer(ES):
    def __init__(self):
        super().__init__()

    def stem(self, word):
        return super().stemWord(word)
    
