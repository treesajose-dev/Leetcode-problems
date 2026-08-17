class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        set1=set(nums)
        n=len(nums)

        natural_sum=n*(n+1)//2
        

        num_sum=sum(nums)
        set1_sum=sum(set1)

        return [num_sum-set1_sum, natural_sum-set1_sum]
        

        