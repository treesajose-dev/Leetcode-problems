class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        lis=list(s.split())
        new_lis=[]
        for i in range(k):
            new_lis.append(lis[i])
            new_lis.append(" ")

        return "".join(new_lis[:-1])



        