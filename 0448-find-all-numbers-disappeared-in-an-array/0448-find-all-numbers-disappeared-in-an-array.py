class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        start=1
        end=len(nums)

        st=set(nums)

        lis=[]

        for i in range(start, end+1):
            if i not in st:
                lis.append(i)

        return lis
        