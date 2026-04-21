class Solution(object):
    def makeGood(self, s):
        stack = []
        
        for char in s:
            if stack and stack[-1] != char and stack[-1].lower() == char.lower() :
                stack.pop()  # remove bad pair
            else:
                stack.append(char)
        
        return "".join(stack)