class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        dict1={}
        lis=[]
        for x in nums:
            if x in dict1:
                dict1[x]+=1
            else:
                dict1[x]=1

        for key,value in dict1.items():
            if value>=2:
                lis.append(key)

        return lis
        