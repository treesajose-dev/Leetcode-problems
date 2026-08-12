class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict1={}
        for char in s:
            if char in dict1:
                dict1[char]+=1
            else:
                dict1[char]=1

        
        lis=dict1.values()
        no=lis[0]

        for x in lis:
            if no!=x:
                return False

        return True

        