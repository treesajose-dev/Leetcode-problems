class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        ans=[0]*(len(nums))
        sum=0
            

        for i in range(0,len(nums)):
            ans[i]=ans[i>>1]+(i & 1)
            if ans[i]==k:
                sum+=nums[i]


        return sum
        