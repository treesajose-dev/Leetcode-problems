class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_power=1
        co=1

        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                co+=1
            else:
                max_power=max(max_power,co)
                co=1

                

        return max(max_power,co)
            