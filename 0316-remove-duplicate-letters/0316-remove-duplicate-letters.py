class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        #lexicographical order means ascending order of alphabets

        #in dict mark the last postion of char

        last_occ={} #dict
        stack=[] #list
        visited=set() #set

        for i in range(len(s)):
            last_occ[s[i]]=i

        for i in range(len(s)):
            if s[i] not in visited:
                while (stack and stack[-1] > s[i] 
                and last_occ[stack[-1]]>i ):
                    visited.remove(stack.pop())
                stack.append(s[i])
                visited.add(s[i])
        return ''.join(stack)
        

