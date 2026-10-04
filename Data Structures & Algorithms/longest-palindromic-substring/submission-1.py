class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        if len(s) <= 1:
            return s
        def expand(i,j):
            nonlocal res
            while i >= 0 and j < len(s) and s[i] == s[j]:
                if j - i + 1 > len(res):
                    res = s[i:j+1]
                i -= 1
                j += 1
            
            
        for i in range(len(s)-1):
            expand(i,i)
            expand(i,i+1)

        return res
                