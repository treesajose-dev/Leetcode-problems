class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_n=max(nums)
        min_n=min(nums)

        for x in nums:
            if x !=max_n and x!=min_n:
                return x
        
        return -1
        