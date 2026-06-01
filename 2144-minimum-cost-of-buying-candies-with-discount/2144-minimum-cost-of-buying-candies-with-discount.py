class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
        cost.sort(reverse=True)
        add=0


        for i in range(1,len(cost)+1):
            if i%3==0:
                continue

            add+=cost[i-1]

        return add