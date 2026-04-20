class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #method 1 O(n2)
        for item in nums:
            if nums.count(item) == 1:
                return item

        #method 2 O(n)
        result = 0
        for num in nums:
            result = result ^ num
        return result
        