class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        
        alpha="abcdefghijklmnopqrstuvwxyz"
        lis=[]

        for word in words:
            sum=0
            for x in word:
                if x in alpha:
                    pos=alpha.find(x)
                sum+=weights[pos]

            lis.append(sum)

        ans=""

        rev="zyxwvutsrqponmlkjihgfedcba"

        for x in lis:
            ans+=rev[x%26]

        return ans
        