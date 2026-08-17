class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        co=0
        temp=word
        while temp in sequence:
            temp=temp+word
            co+=1

        return co