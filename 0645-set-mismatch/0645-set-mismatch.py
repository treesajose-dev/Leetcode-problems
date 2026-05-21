class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n=len(nums)

        lis=[]

        dict1={}

        for x in nums:
            if x in dict1:
                dict1[x]+=1
                lis.append(x)
            else:
                dict1[x]=1

        for y in range(1,n+1):
            if y not in nums:
                lis.append(y)

        return lis
        

        