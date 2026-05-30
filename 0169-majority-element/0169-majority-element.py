class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dict1=dict()

        for x in nums:
            if x in dict1:
                dict1[x]+=1
            else:
                dict1[x]=1

        for key,value in dict1.items():
            if value>(len(nums)//2):
                return key