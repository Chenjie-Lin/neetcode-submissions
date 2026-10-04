class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])

        minHeap = [[grid[0][0],0,0]]

        visited = {(0,0)}

        res = []

        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        i = j = 0

        t = 0

        while minHeap:

            while minHeap and minHeap[0][0] <= t:

                val, i, j = heapq.heappop(minHeap)

                res.append(val)
                
                if i == rows - 1 and j == cols - 1:
                    return max(res)

                for dr,dc in directions:
                    r = i + dr
                    c = j + dc

                    if ((r) in range(rows) and (c) in range(cols) and
                        (r, c) not in visited):
                        heapq.heappush(minHeap,[grid[r][c],r,c])
                        visited.add((r,c))
            t += 1

        return max(res)

        

