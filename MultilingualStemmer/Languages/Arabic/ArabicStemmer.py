from snowballstemmer import ArabicStemmer as AS

class ArabicStemmer(AS):
    def __init__(self):
        super().__init__()

    def stem(self, word):
        return super().stemWord(word)
    
