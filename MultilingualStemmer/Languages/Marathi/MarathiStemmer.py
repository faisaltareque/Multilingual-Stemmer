import codecs
import re

class MarathiStemmer:
    """
    This class implements the Marathi Stemmer.
    """
    def __init__(self):
        self.suffixes = {
            1: [u"ो",u"े",u"ू",u"ु",u"ी",u"ि",u"ा",u"च"],
            2: [u"चा",u"चे",u"ने",u"नी",u"ना",u"ते",u"ीं",u"तील",u"ात",u"ाँ",u"ां",u"ों",u"ें",u"तच",u"ता",u"ही",u"ले"],
            3: [u"ाचा",u"ाचे",u"तील",u"ानी",u"ाने",u"ाना",u"ाते",u"ाती",u"ाता",u"तीं",u"तून",u"तील",u"तही",u"तपण",u"कडे",u"ातच",u"हून",u"पणे",u"ाही",u"ाले"],
            4: [u"मधले",u"ातील",u"च्या",u"न्या",u"ऱ्या",u"ख्या",u"वर",u"साठी",u"ातून",u"कडून",u"मुळे",u"वरून",u"ातील",u"नीही",u"ातही",u"ातपण",u"ाकडे",u"पाशी",u"ाहून",u"ापणे",u"मधला"],
            5: [u"ामधले",u"ाच्या",u"ान्या",u"ाऱ्या",u"ाख्या",u"ावर",u"ासाठी",u"पासून",u"ाकडून",u"ामुळे",u"ावरून",u"कडेही",u"ानीही",u"ापाशी",u"ामधला",u"मध्ये"],
            6: [u"पर्यंत",u"ापासून",u"ाकडेही",u"पूर्वक",u"लेल्या",u"ामध्ये"],
            7: [u"ापर्यंत",u"प्रमाणे",u"तसुद्धा",u"ापूर्वक",u"ालेल्या"],
            8: [u"ाप्रमाणे",u"ातसुद्धा"],
        }

    def stem(self, word):
        """
        This function stems the given word.
        """
        for i in range(8,0,-1):
            if len(word) > i + 1:
                for suf in self.suffixes[i]:
                    if word.endswith(suf):
                        word=word[:-i]
        return word