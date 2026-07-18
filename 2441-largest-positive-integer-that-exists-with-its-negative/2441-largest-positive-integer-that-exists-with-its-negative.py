class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lis=[]
        for x in nums:
            if -(x) in nums:
                lis.append(abs(x))

        if lis:
            return max(lis)        
        else:
            return -1
        