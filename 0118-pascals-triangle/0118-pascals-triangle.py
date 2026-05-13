class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        dp=[]
        dp.append([1])
        if numRows==1:
            return dp

        dp.append([1,1])

        if numRows==2:
            return dp

        for i in range(3, numRows + 1):
            prev = dp[i-2]
            temp = [1]

            for j in range(len(prev)-1):
                temp.append(prev[j] + prev[j+1])

            temp.append(1)
            dp.append(temp)

        return dp