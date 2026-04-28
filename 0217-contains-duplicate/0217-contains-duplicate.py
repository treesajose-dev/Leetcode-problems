class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        dict1={}

        for item in nums:
            if item in dict1:
                dict1[item]+=1
            else:
                dict1[item]=1

        print(dict1)

        for item in dict1:
            if dict1[item]>=2:
                return True
        
        return False