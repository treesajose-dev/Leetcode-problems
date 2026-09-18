class Solution(object):
    def sumDivisibleByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        dict1={}
        sum=0
        for x in nums:
            if x in dict1:
                dict1[x]+=1
            else:
                dict1[x]=1
        
        for key,value in dict1.items():
            if value%k==0:
                sum+=(value*key)
        
        return sum
        

        