class Solution(object):
    def digitCount(self, num):
        """
        :type num: str
        :rtype: bool
        """
        ans_co=0

        for i in range(len(num)):
            co=0
            for x in num:
                if x==str(i):
                    co+=1
            if co!=int(num[i]):
                return False
            else:
                ans_co+=1

        if ans_co==len(num):
            return True
        else:
            return False  

            




        
        