class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        lis=[]
        for account in accounts:
            lis.append(sum(account))

        return max(lis)


        