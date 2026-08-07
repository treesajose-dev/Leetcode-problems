class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        co=0
        for row in grid:
             for item in row:
                if item<0:
                    co+=1
        
        return co
        