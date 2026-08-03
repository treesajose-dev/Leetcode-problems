class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        st=""
        for x in words:
            st+=x[0]
        if st==s:
            return True
        else:
            return False