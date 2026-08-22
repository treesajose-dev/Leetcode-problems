class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num=n
        sum_n=0
        prod_n=1

        while num!=0:
            r=num%10
            sum_n+=r
            prod_n*=r
            num=num//10
        
        if n%(sum_n+prod_n)==0:
            return True
        else:
            return False
        