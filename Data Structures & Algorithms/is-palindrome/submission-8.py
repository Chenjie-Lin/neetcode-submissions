class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s)).lower()
        mid = len(s) // 2        
        def expandfrommid(start, end):
            while start >= 0 and end < len(s):
                if s[start] != s[end]:
                    return False
                start -= 1
                end += 1
            return True
        if len(s) % 2 == 0:
            return expandfrommid(mid-1, mid)
        else:
            return expandfrommid(mid, mid)