from PersianStemmer import PersianStemmer as PS

class PersianStemmer(PS):
    def __init__(self):
        super().__init__()

    def stem(self, word):
        return super().run(word)

