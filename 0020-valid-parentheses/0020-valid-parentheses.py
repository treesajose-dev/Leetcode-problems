class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = ['a']
    
        for char in s:
            if (char==')' and stack[-1]=='(') :  # closing bracket
                stack.pop()
            elif (char=='}' and stack[-1]=='{') :  # closing bracket
                stack.pop()
            elif (char==']' and stack[-1]=='[') :  # closing bracket
                stack.pop()
            else:  # opening bracket
                stack.append(char)

        if len(stack)==1:
            return True
        else:
            return False
    


