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
            nxt = node[ch]

            if "$" in nxt:
                res.append(nxt["$"])
                nxt.pop("$")

            

            path.add((r,c))
            
            dfs(r + 1, c, nxt) 
            dfs(r, c+1, nxt)
            dfs(r-1, c, nxt) 
            dfs(r, c-1, nxt) 

            path.remove((r,c))
            


        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        
        return res
        
        