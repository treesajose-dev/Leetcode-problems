class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        common = words[0]

        for word in words[1:]:
            temp = ""
            w = list(word)

            for ch in common:
                if ch in w:
                    temp += ch
                    w.remove(ch)

            common = temp

        return list(common)
