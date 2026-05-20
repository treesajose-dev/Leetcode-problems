class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """

        co=0

        for item in stones:
            if item in jewels:
                co+=1

        return co

        