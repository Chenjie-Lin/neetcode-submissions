class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        rows = [[] for _ in range(n)]
        cols = [[] for _ in range(n)]
        res = []

        def dfs(i):
            if i == n:
                res.append(["".join(row) for row in board])
                return
            for j in range(n):
                if check(i,j):
                    board[i][j] = "Q"
                    rows[i].append("Q")
                    cols[j].append("Q")
                    dfs(i+1)
                    board[i][j] = "."
                    rows[i].pop()
                    cols[j].pop()
                

        def check(i,j):
            if "Q" in rows[i] or "Q" in cols[j]:
                return False

            i1 = i
            j1 = j
            while i1 < n and j1 < n:
                if board[i1][j1] == "Q":
                    return False
                i1 += 1
                j1 += 1
            
            i1 = i
            j1 = j
            
            while i1 >= 0 and j1 >= 0:
                if board[i1][j1] == "Q":
                    return False
                i1 -= 1
                j1 -= 1
            
            i1 = i
            j1 = j

            while i1 < n and j1 >= 0:
                if board[i1][j1] == "Q":
                    return False
                i1 += 1
                j1 -= 1

            i1 = i
            j1 = j
            
            while i1 >= 0 and j1 < n:
                if board[i1][j1] == "Q":
                    return False
                i1 -= 1
                j1 += 1

            return True
        dfs(0)
        return res