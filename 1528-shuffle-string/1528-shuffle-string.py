class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        lis=[""]*len(s)
        for i in range(len(s)):
            lis[indices[i]]=s[i]
        return "".join(lis[::])
        