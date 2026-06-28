class Solution(object):
    def duplicateNumbersXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dict1={}
        lis=[]
        ans=0

        for x in nums:
            if x in dict1:
                dict1[x]+=1
            else:
                dict1[x]=1

        for key,value in dict1.items():
            if value==2:
                lis.append(key)

        for x in lis:
            ans=ans^x

        if lis:
            return ans
        else:
            return 0
        