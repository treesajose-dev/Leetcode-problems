class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        co=0

        while n:
            n=n&(n-1)
            co+=1
        
        return co
