class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        dict1={}
        lis=[]

        for x in nums:
            if x in dict1:
                dict1[x]+=1
            else:
                dict1[x]=1
        
        for k in sorted(dict1,key=lambda x:(dict1[x],-x)):
            for i in range(dict1[k]):
                lis.append(k)

        return lis

        