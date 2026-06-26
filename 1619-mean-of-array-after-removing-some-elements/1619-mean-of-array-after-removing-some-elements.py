class Solution(object):
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """
        arr.sort()

        k = len(arr) // 20

        arr2 = arr[k:len(arr)-k]

        return float(sum(arr2)) / len(arr2)
        