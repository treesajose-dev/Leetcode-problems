class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
    #powers of 2 will have only one 1 in their binary form so removing it will give 0.

        return n>0 and (n & (n-1))==0

