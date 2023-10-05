"""
This stemmer is developed by Simran Kaur. https://github.com/SimranKaur-23.
"""
class PunjabiStemmer:

    """
    This class is used to stem the Punjabi words.
    """

    def __init__(self):
        self.suffixes = {1: ["ੀ ਆਂ ", "िਆਂ", "ੂਆਂ", "ੀ ਏ", "ੀ ਓ"],
                         2: ["ਈ", "ੇ", "ू", "ु", "ी","ਏ", "ि", "ा", "ੋ", "ਜ", "ਜ਼", "ਸ"],
                         3: ["िਓ", "ਾ ਂ", "ੀ ਂ", "ੋ ਂ","ਏ"],
                         4: ["ਿਉ ਂ", "ਵਾਂ" ],
                         5: ["ੀ ਆ", "िਆ", "ਈਆ"]}

    def rreplace(self,string, old, new, count=None):
      """
      This function is used to replace the old string with new string.
      """
      string_reverse = string[::-1]
      old_reverse = old[::-1]
      new_reverse = new[::-1]
      if count:
          final_reverse = string_reverse.replace(old_reverse, new_reverse, count)
      else:
          final_reverse = string_reverse.replace(old_reverse, new_reverse)
      result = final_reverse[::-1]
      return result
    
    def gen_replacement(self, suf, L):
        """
        This function is used to generate the replacement string.
        """
        if L == 1 or L == 5:
            return suf[1:]
        return suf

    def stem(self, text):
        """
        This function is used to stem the Punjabi words.
        """
        tag = [1,2,3,4,5]
        tag.reverse()
        dic_punj = {}
   
        for word in text.split():
            flag = 0
            for L in tag:
                if flag == 1:
                    break
                if len(word) > L + 1:  #checking for minimum 3 letter words
                    for suf in self.suffixes[L]:
                        if word.endswith(suf):
                            word1 = self.rreplace(word,self.gen_replacement(suf,L), '', 1)
                            dic_punj[word] = word1
                            flag = 1
                            break
            if flag == 0:
                #for word length less than 3 (stop words)
                dic_punj[word] = word
        return dic_punj