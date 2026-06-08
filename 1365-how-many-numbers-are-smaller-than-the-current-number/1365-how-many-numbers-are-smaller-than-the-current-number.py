class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        lis=[]

        for i in range(len(nums)):
            co=0
            for j in range(len(nums)):
                if nums[j]<nums[i]:
                    co+=1
            lis.append(co)

        return lis
        