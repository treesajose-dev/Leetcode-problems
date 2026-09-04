class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(len(nums)):
            max_n=max(nums[0:i+1])
            min_n=min(nums[i:])
            if (max_n-min_n)<=k:
                return i
        return -1
        