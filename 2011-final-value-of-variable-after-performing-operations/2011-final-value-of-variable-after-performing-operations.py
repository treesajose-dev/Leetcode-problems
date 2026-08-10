class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        ans=0
        for row in operations:
            if "--" in row:
                ans-=1
            if "++" in row:
                ans+=1
        return ans
        