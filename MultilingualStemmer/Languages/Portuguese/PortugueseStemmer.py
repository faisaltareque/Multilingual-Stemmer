from snowballstemmer import PortugueseStemmer as PS

class PortugueseStemmer(PS):
    def __init__(self):
        super().__init__()

    def stem(self, word):
        return super().stemWord(word)
    
