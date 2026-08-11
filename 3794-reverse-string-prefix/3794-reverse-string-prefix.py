class Solution(object):
    def reversePrefix(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k<=len(s) and k>1:
            lis=s[:k]
            return lis[::-1]+s[k:]
        else:
            return s


        