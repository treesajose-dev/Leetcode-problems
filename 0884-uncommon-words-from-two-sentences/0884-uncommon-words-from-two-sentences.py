class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        
        lis1=list(map(str, s1.split()))
        lis2=list(map(str, s2.split()))
        lis3=[]

        for x in lis2:
            lis1.append(x)

        dict1={}

        for x in lis1:
            if x in dict1:
                dict1[x]+=1
            else:
                dict1[x]=1
        
        for key,value in dict1.items():
            if value==1:
                lis3.append(key)

        return lis3
        