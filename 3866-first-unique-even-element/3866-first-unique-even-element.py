class Solution(object):
    def firstUniqueEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}

        # Count frequencies
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Find the first unique even number
        for num in nums:
            if num % 2 == 0 and count[num] == 1:
                return num

        return -1
        