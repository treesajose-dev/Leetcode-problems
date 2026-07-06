class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        lis=[]
        for i in range(len(words)):
            if x in words[i]:
                lis.append(i)
        
        return lis