class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        oddlis=[]
        evenlis=[]
        odd=1
        even=2

        for i in range(n):
            oddlis.append(odd)
            odd+=2
            evenlis.append(even)
            even+=2

        a=sum(evenlis)
        b=sum(oddlis)

        while (b != 0):
            temp = b
            b = a % b
            a = temp
        
        return a