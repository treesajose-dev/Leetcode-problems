class Solution(object):
    def isAdjacentDiffAtMostTwo(self, s):
        """
        :type s: str
        :rtype: bool
        """

        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if abs(int(s[i])-int(s[i+1]))>2:
                    return False
        return True
        