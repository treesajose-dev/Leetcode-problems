class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        num=""

        for x in digits:
            num+=str(x)

        
        dig=int(num)
        dig+=1

        lis=[]
        while dig!=0:
            rem=dig%10
            lis.append(rem)
            dig=dig//10

        return lis[::-1]
        