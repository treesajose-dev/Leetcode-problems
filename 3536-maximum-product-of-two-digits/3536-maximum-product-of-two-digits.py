class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        lis=[]
        while n!=0:
            r=n%10
            lis.append(r)
            n=n//10

        maxm=0
        for i in range(len(lis)):
            for j in range(i+1,len(lis)):
                maxm=max(maxm,lis[i]*lis[j])

        return maxm


        