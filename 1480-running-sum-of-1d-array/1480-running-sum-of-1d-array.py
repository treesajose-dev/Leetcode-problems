class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lis=[]
        for i in range(len(nums)):
            j=0
            ans=0
            while j<=i:
                ans+=nums[j]
                j+=1
            lis.append(ans)

        return lis
        