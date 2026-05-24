class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        dict1={}
        lis=[]

        for x in arr:
            if x in dict1:
                dict1[x]+=1
            else:
                dict1[x]=1

        print(dict1)

        for key,value in dict1.items():
            if key==value:
                lis.append(key)

        lis.sort()
                
        if not lis:
            return -1

        if len(lis)==1:
            return lis[0]
        else:
            return lis[-1]


        