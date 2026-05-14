class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        s = set()
        not_judge = set()

        for i in range(1, n + 1):
            s.add(i)

        trusted_count = {}

        for i in range(1, n + 1):
            trusted_count[i] = 0

        for item in trust:

            a = item[0]
            b = item[1]

            not_judge.add(a)

            trusted_count[b] += 1

        possible = s.difference(not_judge)

        for person in possible:

            if trusted_count[person] == n - 1:
                return person

        return -1
                

        