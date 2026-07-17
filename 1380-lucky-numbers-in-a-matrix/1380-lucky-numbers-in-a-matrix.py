class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        lis = []
        for i in range(len(matrix)):
            min1 = min(matrix[i])
            for j in range(len(matrix[i])):
                if matrix[i][j] == min1:
                    flag = 1
                    for k in range(len(matrix)):
                        if matrix[k][j] > min1:
                            flag = 0
                            break
                    if flag == 1:
                        lis.append(min1)
        return lis
        