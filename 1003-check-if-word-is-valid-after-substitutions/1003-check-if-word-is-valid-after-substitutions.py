class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]

        for ch in s:
            if ch == 'c':
                if len(stack)<2 or stack.pop()!='b' or stack.pop()!='a':
                    return False
            else:
                stack.append(ch)

        return not stack
        