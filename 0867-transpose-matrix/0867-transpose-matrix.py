class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m=len(matrix)
        n=len(matrix[0])
        mat=[]

        for i in range(n):
            mat.append([0]*m)

        for i in range(0,m):
            for j in range(0,n):
                mat[j][i]=matrix[i][j]

        return mat
        