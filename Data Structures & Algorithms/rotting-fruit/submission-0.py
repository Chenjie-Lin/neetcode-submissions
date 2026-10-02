class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c,0))
        max_t = 0
        while q:
            row, col, t = q.popleft()
            max_t = max(max_t,t)
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            for dr, dc in directions:
                r, c = row + dr, col +dc
                if(r in range(rows) and c in range(cols)
                    and grid[r][c] == 1):
                    q.append((r,c,t+1))
                    grid[r][c] = 2

        if any(1 in row for row in grid):
            return -1
        else:
            return max_t
