class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st=[]

        for x in s:
            st.append(x)
            
            if st[-3:]==['a','b','c']:
                st.pop()
                st.pop()
                st.pop()

        return len(st)==0
        