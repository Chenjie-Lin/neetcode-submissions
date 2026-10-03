class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if n == 0:
            return True

        edgeMap = {i: [] for i in range(n)}

        for a, b in edges:
            edgeMap[a].append(b)
            edgeMap[b].append(a)

        visit = set()

        def dfs(node, prev):

            if node in visit:
                return False

            visit.add(node)

            for path in edgeMap[node]:
                if path != prev:
                    if not dfs(path, node):
                        return False

            return True

        return dfs(0, -1) and len(visit) == n

