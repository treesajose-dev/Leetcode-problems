class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """

        co=0

        alph=[]

        for x in allowed:
            alph.append(x)
        print(alph)

        for x in words:
            flag=1
            for ch in x:
                if ch not in alph:
                    flag=0
                    break
            
            if flag==1:
                co+=1

        return co
        