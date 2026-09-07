class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        ans=0
        for word in words:
            co=0
            ch=chars
            for w in word:
                if w in  ch:
                    ch=ch.replace(w,"",1)
                    co+=1
            if len(word)==co:
                ans+=co
        return ans
        