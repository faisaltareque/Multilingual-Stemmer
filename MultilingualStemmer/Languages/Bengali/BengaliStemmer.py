from bangla_stemmer.stemmer.stemmer import BanglaStemmer

import sys
import os

def suppress_print(func):
    def wrapper(*args, **kwargs):
        original_stdout = sys.stdout
        sys.stdout = open('temp_file', 'w')        
        try:
            result = func(*args, **kwargs)
        finally:
            sys.stdout = original_stdout
            os.remove('temp_file')        
        return result
    return wrapper


class BengaliStemmer(BanglaStemmer):
    def __init__(self):
        super().__init__()

    @suppress_print
    def stem(self, *args, **kwargs):
        return super().stem(*args, **kwargs)
    

