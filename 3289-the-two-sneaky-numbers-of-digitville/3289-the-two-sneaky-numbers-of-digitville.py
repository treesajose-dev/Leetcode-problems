class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dict1={}
        lis=[]

        for x in nums:
            if x in dict1:
                dict1[x]+=1
                if dict1[x]==2:
                    lis.append(x)
            else:
                dict1[x]=1
        return lis