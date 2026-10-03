class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        res = 0
        
        edgeMap = {i: [] for i in range(n)}

        for a, b in edges:
            edgeMap[a].append(b)
            edgeMap[b].append(a)

        visit = set()

        def dfs(node, prev):
            nonlocal res
            if node in visit:
                return 

            visit.add(node)

            for path in edgeMap[node]:
                dfs(path, node)

        for i in range(n):
            if i not in visit:
                dfs(i, i-1)
                res += 1
        return res    

        
