class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        if len(s) <= 1:
            return s
        def expand(i,j):
            nonlocal start, end
            while i >= 0 and j < len(s) and s[i] == s[j]:
                if j - i + 1 > end-start + 1:
                    start, end = i, j
                i -= 1
                j += 1
            
            
        for i in range(len(s)-1):
            expand(i,i)
            expand(i,i+1)

        return s[start:end+1]
                