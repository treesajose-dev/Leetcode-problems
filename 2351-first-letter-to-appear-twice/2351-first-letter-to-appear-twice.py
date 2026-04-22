class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = {} 
        
        # Count frequency of each character 
        for ch in s: 
            if ch in freq: 
                freq[ch] +=1
                if freq[ch]==2:
                    return ch 
            else: 
                freq[ch]=1 
