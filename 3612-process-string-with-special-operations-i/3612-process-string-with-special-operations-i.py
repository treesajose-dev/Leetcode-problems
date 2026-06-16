class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        result=[]

        for char in s:
            if char>='a' and char<='z':
                result.append(char)
            if char=="*" and result:
                result.pop()
            if char=="#" and result:
                result+=result
            if char=="%":
                result.reverse()

        return "".join(result)

        