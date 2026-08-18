class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[0]*(n+1)
        dp[0]=0
        dp[1]=1
        dp[2]=1
        for i in range (3,n+1):
            k=1
            j=i-1   
            while k<=j:         
                k_value=max(k,dp[k])
                j_value=max(j,dp[j])
                dp[i]=max(dp[i],k_value*j_value)
                k+=1
                j-=1

        return max(dp)

        