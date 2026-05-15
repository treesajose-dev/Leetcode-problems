class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos_co=0
        neg_co=0

        for x in nums:
            if x>0:
                pos_co+=1
            elif x<0:
                neg_co+=1
            else:
                continue

        return max(pos_co,neg_co)

        