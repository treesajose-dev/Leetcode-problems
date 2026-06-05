class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dict1={}
        sum=0

        for x in nums:
            if x in dict1:
                dict1[x]+=1
            else:
                dict1[x]=1

        for key,value in dict1.items():
            if value==1:
                sum+=key

        return sum
        