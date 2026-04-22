class Solution(object):
    def firstUniqChar(self, s):
        freq = {}
        
        # Count frequency of each character
        for ch in s:
            if ch in freq:
                freq[ch] +=1
            else:
                freq[ch]=1
        
        # Find first unique character with count=1
        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i
        
        return -1