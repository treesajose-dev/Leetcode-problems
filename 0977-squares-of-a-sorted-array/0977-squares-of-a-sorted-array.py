class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        squares = [n * n for n in nums]
        
        squares.sort()

        return squares