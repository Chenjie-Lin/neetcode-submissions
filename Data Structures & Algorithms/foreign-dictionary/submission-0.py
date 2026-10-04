class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(set)
        chars = set()
        for word in words:
            for ch in word:
                chars.add(ch)

        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if j >= len(words[i+1]):
                    return ""
                if words[i][j] != words[i+1][j]:
                    adj[words[i][j]].add(words[i+1][j])
                    break
        
        res = []
        visit = set()
        done = set()

        def dfs(c):
            if c in visit:
                return False
            if c in done:
                return True

            visit.add(c)

            for nxt in adj[c]:
                if not dfs(nxt):
                    return False

            done.add(c)
            visit.remove(c)
            adj[c] = []
            res.append(c)
            return True

        for c in chars:
            if not dfs(c):
                return ""

        return "".join(reversed(res))
            

                

                

