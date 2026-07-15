class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """

        a=n*n
        b=n*(n+1)

        while (b != 0):
            temp = b
            b = a % b
            a = temp
        
        return a