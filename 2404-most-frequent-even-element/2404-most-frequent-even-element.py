class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}

        for x in nums:
            if x % 2 == 0:
                freq[x] = freq.get(x, 0) + 1

        if not freq:
            return -1

        ans = -1
        max_freq = 0

        for num, count in freq.items():
            if count > max_freq:
                max_freq = count
                ans = num
            elif count == max_freq and num < ans:
                ans = num

        return ans