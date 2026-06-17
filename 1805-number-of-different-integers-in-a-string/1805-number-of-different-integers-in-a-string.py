class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        s=""
        for x in word:

            if x.isdigit():
                s += x

            else:
                s += " "

        st = set()

        for num in s.split():

            st.add(str(int(num)))
        return len(st)
        