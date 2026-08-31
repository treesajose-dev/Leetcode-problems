class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        co=0
        while num!=0:
            co+=1
            if num%2==0:
                num=num//2   
            else:
                num=num-1
        return co