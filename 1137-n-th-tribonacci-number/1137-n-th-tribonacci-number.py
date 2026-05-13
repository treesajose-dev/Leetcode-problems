class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """

        lis=[0]

        if n==0:
            return lis[0]
        lis.append(1)
        if n==1:
            return lis[1]
        lis.append(1)
        if n==2:
            return lis[2]
        
        for i in range(3,n+1):
            lis.append(lis[-1]+lis[-2]+lis[-3])

        return lis[-1]

        
        