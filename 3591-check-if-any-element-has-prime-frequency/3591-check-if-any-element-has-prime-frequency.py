class Solution(object):
    def checkPrimeFrequency(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict1={}

        for x in nums:
            if x in dict1:
                dict1[x]+=1
            else:
                dict1[x]=1
        
        def isPrime(n):
            if n < 2:
                return False

            for i in range(2, n//2 + 1):
                if n % i == 0:
                    return False

            return True

        for value in dict1.values():
            if isPrime(value):
                return True

        return False
        