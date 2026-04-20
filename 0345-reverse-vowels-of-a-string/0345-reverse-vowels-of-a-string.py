class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        st=list(s)
        i=0
        j=len(st)-1

        vowels="aeiouAEIOU"

        while(i<j):
            if st[i] in vowels and st[j] in vowels:
                st[i],st[j]=st[j],st[i]
                i+=1
                j-=1
            elif st[i] not in vowels:
                i+=1
            else:
                j-=1

        return "".join(st) 
            