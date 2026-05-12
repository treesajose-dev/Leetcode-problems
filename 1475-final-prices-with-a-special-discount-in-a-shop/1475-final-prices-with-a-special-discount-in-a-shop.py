class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        newlis=[]
        for i in range(len(prices)):
            disc=0
            for j in range(i+1,len(prices)):
                if prices[j]<=prices[i]:
                    disc=prices[j]
                    break
            
            newlis.append(prices[i]-disc)
        
        return newlis

        