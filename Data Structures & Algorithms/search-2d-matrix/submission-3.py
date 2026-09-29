class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)    
        m = len(matrix[0])    
        j1, j2 = 0, n - 1     
        i1, i2 = 0, m - 1      
        while j1 <= j2:
            midj = (j1 + j2) // 2
            if midj < n - 1 and (matrix[midj][0] < target < matrix[midj+1][0]):
                break
            elif midj == n - 1 and target < matrix[midj][0]:
                break
            elif target > matrix[midj][0]:
                j1 = midj + 1
            elif target < matrix[midj][0]:
                j2 = midj - 1
            else:
                return True
        while i1 <= i2:
            midi = (i1 + i2) // 2
            if target < matrix[midj][midi]:
                i2 = midi - 1
            elif target > matrix[midj][midi]:
                i1 = midi + 1
            else:
                return True
        return False