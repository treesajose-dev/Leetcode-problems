class MinStack(object):

    def __init__(self):
        self.s=[]
        self.st=[]

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.s.append(val)
        # if min stk is empty or val is less than -1 pos in min stk
        if not self.st or (val<= self.st[-1]):
            self.st.append(val)

    def pop(self):
        """
        :rtype: None
        """
        # if element to be popped from s is smallest ie; in st -1 pos 
        # then pop it too.
        if self.s.pop() == self.st[-1]:
            self.st.pop()

    def top(self):
        """
        :rtype: int
        """
        #return -1 if not self.s else self.s[-1]
        if self.s:
            return self.s[-1]
        else:
            return -1

    def getMin(self):
        """
        :rtype: int
        """
        #return -1 if not self.st else self.st[-1]
        if self.st:
            return self.st[-1]
        else:
            return -1


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()