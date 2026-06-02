class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """

        s="balloon"
        dict1={}

        for x in text:
            if x in dict1:
                dict1[x]+=1
            else:
                dict1[x]=1
        
        b = dict1.get('b', 0)
        a = dict1.get('a', 0)
        l = dict1.get('l', 0) // 2
        o = dict1.get('o', 0) // 2
        n = dict1.get('n', 0)

        return min(b, a, l, o, n)


        