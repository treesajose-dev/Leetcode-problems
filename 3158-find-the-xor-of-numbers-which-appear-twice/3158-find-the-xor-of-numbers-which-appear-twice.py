class Solution(object):
    def duplicateNumbersXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        lis=[]
        dup=0

        for i in nums:
            if i in lis:
                dup=dup^i
            lis.append(i)
        return dup        