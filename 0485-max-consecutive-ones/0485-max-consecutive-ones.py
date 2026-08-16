class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        co=0
        lis=[]
        for i in range(len(nums)):
            if nums[i]==1:
                co+=1
            else:
                lis.append(co)
                co=0
        lis.append(co)

        return max(lis)

        
        