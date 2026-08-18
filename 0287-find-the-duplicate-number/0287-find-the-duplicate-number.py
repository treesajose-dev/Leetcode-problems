class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l, r = 1, len(nums)-1
        
        while l+1 <= r:
            mid, count = (l+r)//2,0
            for num in nums:
                if num <= mid:
                    count+=1
            
            if count<=mid:
                l=mid+1
            else:
                r=mid

        return r





        