class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        # odd numbers right shift one 1 is gone
        # even numbers right shift no. of ones remains same

        # odd nos & 1 gives 1
        #even nos & 1 gives 0

        ans=[0]*(n+1)

        for i in range(1,n+1):
            ans[i]=ans[i>>1] + (i & 1)

        return ans
        