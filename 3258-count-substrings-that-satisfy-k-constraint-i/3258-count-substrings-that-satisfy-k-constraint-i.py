class Solution(object):
    def countKConstraintSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res, l, ones=0,0,0

        for r,n in enumerate(s):
            ones+=1 if n=='1' else 0
            while ones > k and r-l+1 -ones >k:
                ones-=1 if s[l] == '1' else 0
                l+=1
            res+=r-l+1
        return res
        