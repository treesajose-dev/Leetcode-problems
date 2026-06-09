class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """

        set1=set()

        for x in s:
            if x.isdigit():
                set1.add(int(x))

        lis=list(set1)

        lis.sort()

        if len(lis)<2:
            return -1
        
        return lis[-2]
            
            
    
        