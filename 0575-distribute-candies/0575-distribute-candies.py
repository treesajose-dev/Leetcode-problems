class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """

        candy=len(candyType)//2

        no=len(set(candyType))

        if candy<=no:
            return candy
        else:
            return no

        