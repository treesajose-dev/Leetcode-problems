class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        dic1 = {}
        dic2 = {}

        for x in words1:
            if x in dic1:
                dic1[x] += 1
            else:
                dic1[x] = 1

        for x in words2:
            if x in dic2:
                dic2[x] += 1
            else:
                dic2[x] = 1

        co = 0

        for x in dic1:
            if dic1[x] == 1 and x in dic2 and dic2[x] == 1:
                co += 1

        return co