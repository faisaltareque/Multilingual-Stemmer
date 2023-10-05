import re


class UrduStemmer:
    """
    This class is used to stem the Urdu words.
    """
    def __init__(self):
        self.urduPrefixes = ['بے', 'بد', 'لا', 'ے', 'نا', 'با', 'کم', 'ان', 'اہل', 'کم']
        self.urduSuffixes = ['دار', 'وں', 'یاں', 'یں', 'ات', 'گوار', 'ور', 'پسند']

    def remove(self, string):
        return string.replace(" ", "")
    
    def stem(self, word, clean=False,chars=None):
        """
        This function is used to stem the given word.
        :param word: The word to be stemmed.
        :param clean: If True, the word is cleaned before stemming.
        :param chars: The characters to be removed from the word before stemming.
        :return: The stemmed word.
        """
        if clean == True:
            word = self.clean_text(word, chars)
        
        ans = word
        found = False
        
        for prefix in self.urduPrefixes:
            checkPrefix = re.search(rf'\A{prefix}', word)
            if checkPrefix:
                ans = word[checkPrefix.span(0)[1]:]
                found = True
                break
        
        if not found:
            for suffix in self.urduSuffixes:
                checkSuffix = re.search(rf"{suffix}\Z", word)
                if checkSuffix:
                    ans = word[:checkSuffix.span(0)[0]]
                    break
        
        return ans
