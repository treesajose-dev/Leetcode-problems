class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        i=word.find(ch)
        upp=i+1

        lis=word[:upp]
        
        return lis[::-1]+word[upp:]
        