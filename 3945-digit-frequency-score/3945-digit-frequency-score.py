class Solution(object):
    def digitFrequencyScore(self, n):
        """
        :type n: int
        :rtype: int
        """
        dict1={}
        ans=0

        lis=list(map(int,str(n)))

        for x in lis:
            if x in dict1:
                dict1[x]+=1
            else:
                dict1[x]=1

        for key,value in dict1.items():
            ans+=key*value

        return ans
        