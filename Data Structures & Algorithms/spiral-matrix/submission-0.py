class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        m = len(matrix)
        n = len(matrix[0])
        l, r = 0, n-1
        t, b = 0, m - 1

        while l <= r and t <= b:

            if l == r:     
                                     
                for i in range(t, b + 1):
                    res.append(matrix[i][l])
                break

            if t == b:                   
                for j in range(l, r + 1):
                    res.append(matrix[t][j])
                break


            i, j = t, l

            while j < r:
                res.append(matrix[i][j])
                j += 1

            while i < b:
                res.append(matrix[i][j])
                i += 1

            while j > l:
                res.append(matrix[i][j])
                j -= 1
                
            while i > t:
                res.append(matrix[i][j])
                i -= 1

            l += 1
            r -= 1
            t += 1
            b -= 1

        return res


            
                




        

