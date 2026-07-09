class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        for i in range(len(nums)+1):
            co=0
            for x in nums:
                if x>=i:
                    co+=1
            if co==i:
                return i
        return -1
        