class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        while len(s) > k:
            ans = ""

            for i in range(0, len(s), k):
                part = s[i:i+k]
                total = 0

                for digit in part:
                    total += int(digit)

                ans += str(total)

            s = ans

        return s