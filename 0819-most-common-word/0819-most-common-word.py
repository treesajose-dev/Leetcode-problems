class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """

        lc = paragraph.lower()
        s = ""

        punct = "!?',;."

        for letter in lc:
            if letter not in punct:
                s += letter
            else:
                s += " "   # replace punctuation with space

        lis = s.split()

        freq = {}

        for word in lis:
            if word not in banned:
                freq[word] = freq.get(word, 0) + 1

        ans = ""
        mx = 0

        for word in freq:
            if freq[word] > mx:
                mx = freq[word]
                ans = word

        return ans

        print(s)

        lis=list(s.split())

        print(lis)
        