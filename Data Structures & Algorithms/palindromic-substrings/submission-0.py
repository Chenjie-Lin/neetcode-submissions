class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        if len(s) <= 1:
            return 1
        def expand(i,j):
            nonlocal count
            while i >= 0 and j < len(s) and s[i] == s[j]:
                count += 1
                i -= 1
                j += 1
            
            
        for i in range(len(s)):
            expand(i,i)
        for i in range(len(s)-1):
            expand(i,i+1)

        return count