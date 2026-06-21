class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])
        if m*n != r*c:
            return mat
        reshape = [[0 for _ in range(c)]for _ in range(r)]
        for i in range(m*n):
            reshape[i//c][i%c] = mat[i//n][i%n]
        return reshape