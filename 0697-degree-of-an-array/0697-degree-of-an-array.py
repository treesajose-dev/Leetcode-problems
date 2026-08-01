class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic={}
        for x in nums:
            if x in dic:
                dic[x]+=1
            else:
                dic[x]=1
        maz = max(dic.values())
        final = len(nums)
        for x in dic:
            if dic[x] == maz:
                l = nums.index(x)
                r = len(nums) - 1 - nums[::-1].index(x)
                final = min(final, r - l + 1)
        return final

        
        