class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """

        dict1={}
        lis=[]

        for i in range(len(heights)):
            dict1[heights[i]]=names[i]

        for x in sorted(dict1,reverse=True):
            lis.append(dict1[x])

        return lis