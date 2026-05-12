class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n==1:
            return True
            
        lis=[]
        lis.append(n)

        for item in lis:
            sum=0
            while item!=0:
                rem=item%10
                sum+=rem*rem
                item=item//10

            if sum in lis:
                return False

            lis.append(sum)

            if 1 in lis:
                return True
            
        