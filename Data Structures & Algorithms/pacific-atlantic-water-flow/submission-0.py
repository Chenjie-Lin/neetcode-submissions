class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        rows, cols = len(heights), len(heights[0])
        atlantic = set()
        pacific = set()

        def dfs(r, c, ocean):

            stack = []
            stack.append((r,c))
            ocean.add((r,c))
            directions = [[1,0], [-1,0], [0,1], [0,-1]]

            while stack:
                row, col = stack.pop()
                for dr, dc in directions:
                    r, c = row + dr, col +dc
                    if(r in range(rows) and c in range(cols) and
                        (r,c) not in ocean and heights[r][c] >= heights[row][col]):
                        stack.append((r,c))
                        ocean.add((r,c))

                

        
        for i in range(rows):
            dfs(i,0,pacific)
        for j in range(cols):
            dfs(0,j,pacific)

        for i in range(rows):
            dfs(i, cols - 1,atlantic)
        for j in range(cols):
            dfs(rows - 1, j,atlantic)
        
        for i in pacific:
            if i in atlantic:
                res.append(i)
        return res