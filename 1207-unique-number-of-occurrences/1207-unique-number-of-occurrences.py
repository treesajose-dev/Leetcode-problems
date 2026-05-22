class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        dict1={}

        for x in arr:
            if x in dict1:
                dict1[x]+=1
            else:
                dict1[x]=1
        
        set1=set(list(dict1.values()))

        print(dict1)

        print(set1)

        arr_len=len(set(arr))
        set1_len=len(set1)

        if arr_len==set1_len:
            return True
        else:
            return False
        