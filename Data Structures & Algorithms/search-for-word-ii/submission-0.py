class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = {}
        for w in words:
            curr = root
            for c in w:
                curr = curr.setdefault(c, {})
            curr["$"] = w

        res = []
        rows, cols = len(board), len(board[0])
        path = set()

        def dfs(r, c, node):
            
            if (r < 0 or c < 0 or 
                r >= rows or c >= cols 
                or board[r][c] not in node
                or (r,c) in path):
                return 

            ch = board[r][c]

            if ch not in node:
                return

            nxt = node[ch]
            if "$" in nxt:
                res.append(nxt.pop("$"))

            path.add((r,c))

            dfs(r + 1, c, nxt) 
            dfs(r, c+1, nxt)
            dfs(r-1, c, nxt) 
            dfs(r, c-1, nxt) 

            if not nxt:
                del node[ch]

            path.remove((r,c))
            
        




        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        
        return res
        
        