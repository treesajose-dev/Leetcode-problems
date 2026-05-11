class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        count = 0
        i=0
        j=0

        for j in range(len(s)):
            if s[j]=='(':
                count+=1
            elif s[j]==')':
                count-=1
            
            if count==0:
                ans+=s[i+1:j]
                i=j+1
        
        return ans
        
            
            

