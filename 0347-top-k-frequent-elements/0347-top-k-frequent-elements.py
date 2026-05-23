class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        dict1={}

        for x in nums:
            if x in dict1:
                dict1[x]+=1
            else:
                dict1[x]=1
        
        lis=[]

        co=0

        for i in sorted(dict1,key=dict1.get,reverse=True):
            if co<k:
                co+=1
                lis.append(i)
        return lis


        