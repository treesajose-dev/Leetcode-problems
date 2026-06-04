class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        expected=[]

        for x in heights:
            expected.append(x)

        heights.sort()

        co=0

        for i in range(len(heights)):
            if heights[i] is not expected[i]:
                co+=1
        
        return co
        