class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        st=str(n)
        num=0
        sum_num=0
        for s in st:
            if s=='0':
                continue
            num=num*10+int(s)
            sum_num+=int(s)
        return num*sum_num
        
        sum_lis=sum(lis)

        number=map(int,lis)
        print(number)