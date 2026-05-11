class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []

        for x in nums:

            temp = []

            while x > 0:
                temp.append(x % 10)
                x //= 10

            ans.extend(temp[::-1])

        return ans