class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows, cols = len(grid), len(grid[0])
        INF = 2147483647
        
        q = collections.deque()

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
        while q:
            row, col = q.popleft()
            directions = directions = [[1,0], [-1,0], [0,1], [0,-1]]
            for dr, dc in directions:
                r, c = row + dr, col +dc
                if(r in range(rows) and c in range(cols)
                    and grid[r][c] == INF):
                    q.append((r,c))
                    grid[r][c] = grid[row][col] + 1

