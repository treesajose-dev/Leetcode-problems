class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # Get unique sorted values
        sorted_unique = sorted(set(arr))

        # Assign ranks
        rank = {}
        for i, num in enumerate(sorted_unique):
            rank[num] = i + 1

        # Build answer in original order
        return [rank[num] for num in arr]