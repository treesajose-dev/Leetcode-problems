class Solution(object):
    def toggleLightBulbs(self, bulbs):
        """
        :type bulbs: List[int]
        :rtype: List[int]
        """
        dic={}
        lis=[]
        for x in bulbs:
            if x in dic:
                dic[x]+=1
            else:
                dic[x]=1
        
        for x,v in dic.items():
            if v%2!=0:
                lis.append(x)
        
        lis.sort()
        return lis
        