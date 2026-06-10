class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """

        dict1={}
        lis=[]
        non=[]

        for x in arr1:
            if x in dict1:
                dict1[x]+=1
            else:
                dict1[x]=1      

        for y in arr2:
            for key,value in dict1.items():
                co=0
                if y == key:
                    while co<value:
                        lis.append(key)
                        co+=1
        
        arr1.sort()

        for z in arr1:
            if z not in arr2:
                lis.append(z)

        return lis
