class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum=0
        l=len(s)
        for i in range(1,l):
            sum+=abs(ord(s[i])-ord(s[i-1]))
        return sum
        