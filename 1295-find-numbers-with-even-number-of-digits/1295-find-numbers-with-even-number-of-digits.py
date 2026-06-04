class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even_co=0
        co=0
        
        for x in nums:
            co=0
            while x:
                x//=10
                co+=1
            
            if co%2==0:
                even_co+=1

        return even_co