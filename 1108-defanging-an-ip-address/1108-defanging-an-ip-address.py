class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        stack=[]
        for x in address:
            if x==".":
                stack.append("[.]")
            else:
                stack.append(x)
        return "".join(stack)

        