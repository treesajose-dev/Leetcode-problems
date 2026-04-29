class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        num = 0
        sign = '+'
        
        for i in range(len(s)):
            ch = s[i]
            
            if ch.isdigit():
                num = num * 10 + int(ch)
            
            # if operator OR last character
            if ch in "+-*/" or i == len(s) - 1:
                # checking done with sign var not ch 
                # (sign var stores prev char whereas ch stores current char. )
                if sign == '+':
                    stack.append(+num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    stack.append(int(float(stack.pop()) / num))  # truncate
                
                sign = ch  #replace sign with current charatcer 
                num = 0    #reset num to 0.
        
        return sum(stack) #finally return sum of stack
