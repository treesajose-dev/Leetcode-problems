class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        num=n

        while num>=n:
            prod=1
            temp=num
            while temp > 0:
                r=temp%10
                prod*=r
                temp=temp//10

            # Handles the case num == 0
            if num == 0:
                prod = 0

            if prod % t == 0:
                return num

            num += 1

        
