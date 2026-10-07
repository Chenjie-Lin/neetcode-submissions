class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for h in range(n):
                        if matrix[i][h] != 0:
                            matrix[i][h] = float("inf") 
                    for v in range(m):
                        if matrix[v][j] != 0:
                            matrix[v][j] = float("inf")

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == float("inf"):
                    matrix[i][j] = 0