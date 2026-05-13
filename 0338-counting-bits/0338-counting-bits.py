class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        ans=[0]*(n+1)

        
        for i in range(n+1):
            temp=i
            co=0
            while temp:
                temp=temp&(temp-1)
                co+=1
            ans[i]=co

        return ans

        