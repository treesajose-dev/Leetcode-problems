class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        small=min(nums)
        large=max(nums)
        lis=[]

        for i in range(1,small+1):
            if small%i==0 and large%i==0:
                lis.append(i)

        return max(lis)


        