class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows,cols = len(matrix),len(matrix[0])
        r,l = [],[]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    r.append(i)
                    l.append(j)
        for i in r:
            for j in range(cols):
                matrix[0][0] = 0
        for i in c:
            for j in range(rows):
                matrix[j][i] = 0
