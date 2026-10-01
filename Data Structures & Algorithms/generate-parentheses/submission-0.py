class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def dfs(left, curr):
            total = len(curr)
            right = total - left
            if total == n * 2:
                res.append(curr)
                return
            
            if left < n:
                curr += "("
                dfs(left+1, curr)
                curr = curr[0:-1]
            
            if right < left:
                curr += ")"
                dfs(left, curr)


        dfs(0, "")
        return res