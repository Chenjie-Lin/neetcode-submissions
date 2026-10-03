class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        visited = set()

        def bfs(r,c):

            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            region = [[r,c]]

            if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                border = True
            else:
                border = False
            while q:

                row, col = q.popleft()

                for dr,dc in directions:

                    r = row + dr
                    c = col + dc

                    if ((r) in range(rows) and (c) in range(cols) and
                        board[r][c] == "O" and (r, c) not in visited):
                        if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                            border = True
                        q.append((r,c))
                        visited.add((r,c))
                        region.append((r,c))
            
            if not border:
                for r, c in region:
                    board[r][c] = "X"
        
        for r in range(rows):
            for c in range(cols):
                if(board[r][c] == "O" and (r,c) not in visited):
                    bfs(r,c)
        
