class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False
            
        edgeMap = {i: [] for i in range(n)}
        for a, b in edges:
            edgeMap[a].append(b)
            edgeMap[b].append(a)

        visit = set()

        def dfs(node):
            if node in visit:
                return False

            visit.add(node)

            for path in edgeMap[node]:
                dfs(path)

        dfs(0)
        return len(visit) == n

