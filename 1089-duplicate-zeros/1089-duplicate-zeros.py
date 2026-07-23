class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        l=len(arr)
        lis=[]
        for x in arr:
            lis.append(x)
            if x==0:
                lis.append(0)
        lis = lis[:l]
        for i in range(l):
            arr[i] = lis[i]
        return arr
        