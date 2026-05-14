class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        size = len(primes)
        ugly=1
        dp=[1]

        index =[0]*size
        ugly_nums=[1]*size

        for i in range(1,n):
            for j in range(0,size):
                if ugly_nums[j]==ugly:
                    ugly_nums[j]=dp[index[j]]*primes[j]
                    index[j]+=1
                
            ugly=min(ugly_nums)
            dp.append(ugly)

        return dp[-1]


            


        