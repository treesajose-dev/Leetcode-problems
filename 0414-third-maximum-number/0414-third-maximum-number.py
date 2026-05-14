class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        s=set(nums)

        lis=list(s)

        for i in range(0,len(lis)):
            for j in range(0,len(lis)-i-1):
                if lis[j]>lis[j+1]:
                    lis[j],lis[j+1]=lis[j+1],lis[j]

        print(lis)

        if len(lis)>2:
            return lis[-3]
        elif len(lis)==2:
            return lis[1]
        else:
            return lis[0]