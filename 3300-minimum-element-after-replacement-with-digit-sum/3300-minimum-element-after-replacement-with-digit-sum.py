class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    
        lis=[]

        for n in nums:
            sum=0
            while n!=0:
                rem=n%10
                sum+=rem
                n=n//10
            lis.append(sum)

        return min(lis)
        
                