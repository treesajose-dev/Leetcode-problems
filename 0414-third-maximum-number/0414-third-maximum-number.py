class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        s=set(nums)

        lis=list(s)

        lis.sort()

        print(lis)

        if len(lis)>2:
            return lis[-3]
        elif len(lis)==2:
            return lis[1]
        else:
            return lis[0]