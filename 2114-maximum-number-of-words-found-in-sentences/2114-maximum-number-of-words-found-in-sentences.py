class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        lis=[]
        for x in sentences:
            lis.append(len(x.split()))

        return max(lis)