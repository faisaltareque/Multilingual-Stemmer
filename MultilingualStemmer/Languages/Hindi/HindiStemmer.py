import re


class HindiStemmer:
    """
    This class is used to stem the Hindi words.
    """
    def __init__(self):
        self.suffixes = {
            1: ["ो", "े", "ू", "ु", "ी", "ि", "ा"],  
            2: ["तृ","ान","ैत","ने","ाऊ","ाव","कर", "ाओ", "िए", "ाई", "ाए", "नी", "ना", "ते", "ीं", "ती", "ता", "ाँ", "ां", "ों", "ें","ीय", "ति","या", "पन", "पा", "ित","ीन","लु","यत","वट","लू"],     
            3: ["ेरा","त्व","नीय","ौनी","ौवल","ौती","ौता","ापा","वास","हास","काल","पान","न्त","ौना","सार","पोश","नाक", "ियल","ैया", "ौटी","ावा","ाहट","िया","हार", "ाकर", "ाइए", "ाईं", "ाया", "ेगी", "वान", "बीन", "ेगा", "ोगी", "ोगे", "ाने", "ाना", "ाते", "ाती", "ाता", "तीं", "ाओं", "ाएं", "ुओं", "ुएं", "ुआं","कला","िमा","कार", "गार", "दान","खोर"],     
            4: ["ावास","कलाप","हारा","तव्य","वैया", "वाला", "ाएगी", "ाएगा", "ाओगी", "ाओगे", "एंगी", "ेंगी", "एंगे", "ेंगे", "ूंगी", "ूंगा", "ातीं", "नाओं", "नाएं", "ताओं", "ताएं", "ियाँ", "ियों", "ियां", "त्वा","तव्य","कल्प","िष्ठ","जादा","क्कड़"],     
            5: ["ाएंगी", "ाएंगे", "ाऊंगी", "ाऊंगा", "ाइयाँ", "ाइयों", "ाइयां", "अक्कड़","तव्य:","निष्ठ"],
        }
        self.words_dict  = {"तैराक":"तैर", "चालाक":"चाल", "कूलाक":"कूल", "बेलन":"बेल", "मिलाप":"मिल", "चुपचाप": "चुप", "निकास":"निकस", "लुकास":"लुक"}
        self.special_suffixes = ["र्", "ज्य","त्य"]
        self.dict_special_suffixes = {"र्":"ृ", "ज्य":"ज्", "त्य":"त्"}

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
        bl = False
        
        if word in self.words_dict.keys():
            return self.words_dict[word]
        
        for L in 5, 4, 3, 2, 1:
            if len(word) > L + 1:
                for suf in self.suffixes[L]:
                    if word.endswith(suf):
                        ans = word[:-L]
                        bl =True
            if bl == True:
                break
                        
        if bl == True:
            for suf in self.suffixes[1]:
                if ans.endswith(suf):
                    # use case - गानेवाला
                    ans = self.stem(ans)
       
        for suf in self.special_suffixes:
            if ans.endswith(suf):
                l = len(suf)
                ans = ans[:-l]
                ans += self.dict_special_suffixes[suf]     
        return ans
    
    def clean_text(self, text, chars=None):
        if chars == None:        
            text = re.sub(r"[()\"#/@;:<>{}`+=~|!?,']", "", text)
        else:
            text = re.sub(r"[" +chars+ "()\"#/@;:<>{}`+=~|!?,']", "", text)
        return text
