class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict1={}
        co=0

        for x in nums:
            if x in dict1:
                dict1[x]+=1
            else:
                dict1[x]=1

        max_val=max(list(dict1.values()))

        for k,v in dict1.items():
            if v==max_val:
                co+=v

        return co
        