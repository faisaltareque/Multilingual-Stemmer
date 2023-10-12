from snowballstemmer import IndonesianStemmer as IS

class IndonesianStemmer(IS):
    def __init__(self):
        super().__init__()

    def stem(self, word):
        return super().stemWord(word)
    
