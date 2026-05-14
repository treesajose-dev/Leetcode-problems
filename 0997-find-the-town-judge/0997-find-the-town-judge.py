class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        IN = [0] * (n + 1)  #vote count
        OUT = [0] * (n + 1) # indexes who are not judges

        for a, b in trust:

            OUT[a] += 1
            IN[b] += 1

        for i in range(1, n + 1):

            if IN[i] == n - 1 and OUT[i] == 0:
                return i

        return -1

        