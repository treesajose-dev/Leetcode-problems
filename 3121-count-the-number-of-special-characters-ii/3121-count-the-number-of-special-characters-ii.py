class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        lc=[]
        uc=[]

        for x in word:
            if x.islower():
                lc.append(x)
            else:
                uc.append(x.lower())

        co=0
        for x in set(lc):
            if x in uc and word.rfind(x) < word.find(x.upper()):
                uc.remove(x)
                co+=1
        
        return co