class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dict1={}

        for ch in t:     
            if ch in dict1:
                dict1[ch]+=1
            else:
                dict1[ch]=1

        for ch in s:
            dict1[ch]-=1
        
        for item in dict1:
            if dict1[item]==1:
                return item


