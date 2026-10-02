class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def ispalindrome(s):
            for i in range(len(s)// 2):
                if s[i] != s[-i -1]:
                    return False
            return True

        part = []

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if ispalindrome(s[i:j+1]):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return res  

