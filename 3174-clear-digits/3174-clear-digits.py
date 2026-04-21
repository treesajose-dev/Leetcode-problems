class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """

        '''
        stack=[]

        nums="1234567890"

        for x in s:
            if stack and (x in nums) and stack[-1].isalpha():
                stack.pop()
            else:
                stack.append(x)

        return "".join(stack) 
        '''

        #method 2
        stack=[]
        for x in s:
            if x.isalpha():
                stack.append(x)
            else:
                stack.pop()

        return "".join(stack) 
