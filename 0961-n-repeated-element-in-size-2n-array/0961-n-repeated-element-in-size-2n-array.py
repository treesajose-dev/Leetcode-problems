class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict1={}
        for x in nums:
            if x in dict1:
                dict1[x]+=1
            else:
                dict1[x]=1
        
        for k,v in dict1.items():
            if v>1:
                return k
        