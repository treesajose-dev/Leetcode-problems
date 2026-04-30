class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict1={}

        for x in nums:
            if x in dict1:
                dict1[x]+=1
            else:
                dict1[x]=1
         
        for key in dict1:
            if dict1[key]!=3:
                return key
