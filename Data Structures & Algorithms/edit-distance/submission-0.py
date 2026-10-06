class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = {}

        def dfs(i,j):
            if i == m and j == n:
                return 0
            if i == m or j == n:
                return max(m-i, n-j)
            if (i,j) in dp:
                return dp[(i,j)]
            
            if word1[i] == word2[j]:
                dp[(i,j)] = dfs(i+1, j+1)
            else:
                insert = dfs(i, j+1) + 1
                remove = dfs(i+1, j) + 1
                replace = dfs(i+1, j+1) + 1
                dp[(i,j)] = min(insert,remove,replace)

            return dp[(i,j)]
        
        return dfs(0,0)
