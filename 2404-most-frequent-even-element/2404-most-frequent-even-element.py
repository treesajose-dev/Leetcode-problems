class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = -1
        max_freq = 0

        for x in nums:
            if x % 2 == 0:
                freq = nums.count(x)

                if freq > max_freq:
                    max_freq = freq
                    ans = x
                elif freq == max_freq:
                    if ans == -1 or x < ans:
                        ans = x

        return ans