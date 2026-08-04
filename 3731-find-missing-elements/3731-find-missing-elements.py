class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        max_n=max(nums)
        min_n=min(nums)
        lis=[]

        for i in range(min_n,max_n+1):
            if i not in nums:
                lis.append(i)

        return lis
        