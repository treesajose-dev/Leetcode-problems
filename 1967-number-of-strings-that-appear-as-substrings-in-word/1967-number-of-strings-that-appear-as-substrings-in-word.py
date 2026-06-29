class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        co=0

        for x in patterns:
            if x in word:
                co+=1
        
        return co