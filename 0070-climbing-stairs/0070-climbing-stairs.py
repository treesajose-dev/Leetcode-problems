class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        pn=0
        nn=0
        cn=1
        i=0

        if n==1:
            return 1 

        while i<n:
            nn=pn+cn
            pn=cn
            cn=nn
            i+=1

        return nn

            



        


            
        
        