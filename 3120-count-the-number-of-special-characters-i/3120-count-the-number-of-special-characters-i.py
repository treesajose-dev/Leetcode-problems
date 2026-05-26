class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        up=set()
        lo=set()

        for x in word:
            if x.islower():
                lo.add(x)
            else:
                up.add(x.lower())

        co=0

        for x in lo:
            if x in up:
                co+=1

        return co
