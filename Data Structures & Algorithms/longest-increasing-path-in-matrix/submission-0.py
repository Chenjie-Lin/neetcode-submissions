class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix) # height
        n = len(matrix[0]) # width
        # dp = [[1] * (n+1) for _ in range(m+1)]
        dp = {}
        def dfs(i,j):

            if (i,j) in dp:

                return dp[(i,j)]

            directions = [[0,1], [0,-1], [1,0], [-1,0]]
            dp[(i,j)] = 1
            for dr, dc in directions:
                r = i + dr
                c = j + dc
                if ((0 <= r < m) and (0 <= c < n) and matrix[i][j] < matrix[r][c]):

                    dp[(i,j)] = max(dfs(r,c) + 1, dp[i,j])
            
            return dp[(i,j)]
        
        best = 0
        for i in range(m):
            for j in range(n):
                best = max(dfs(i,j), best)
        
        return best
            
        



