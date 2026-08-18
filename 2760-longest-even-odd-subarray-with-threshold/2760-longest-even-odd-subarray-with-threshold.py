class Solution(object):
    def longestAlternatingSubarray(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        ans=0
        co=0
        for i in range(len(nums)):
            if nums[i] <= threshold and nums[i]%2==0:
                co=1
                for j in range(i+1,len(nums)):
                    if nums[j] <=threshold and nums[j]%2!=nums[j-1]%2:
                        co+=1
                    else:
                        break
                ans=max(ans,co)
            else:
                co=0
        return ans


        
        