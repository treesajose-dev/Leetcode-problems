class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        l = len(pref)
        co = 0
        for x in words:
            if len(x) >= l:
                flag = 1
                for i in range(l):
                    if pref[i] != x[i]:
                        flag = 0
                        break
                if flag == 1:
                    co += 1
        return co