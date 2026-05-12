class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        while len(stones)>1:
            stones.sort()

            x=stones.pop()
            y=stones.pop()

            if x != y:
                stones.append(x - y)

        if stones:
            return stones[0]
            
        return 0