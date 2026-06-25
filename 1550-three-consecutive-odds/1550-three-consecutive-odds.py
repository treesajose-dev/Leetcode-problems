class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        stk=[]
        for x in arr:
            if len(stk) >= 2 and stk[-1]%2!=0 and stk[-2]%2!=0 and x%2!=0:
                stk.pop()
                stk.pop()
                return True
            stk.append(x)
                
        return False
        