class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        n = len(s)
        dp = {-1: 1, 0: 1}

        for i in range(1, n):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i-1]
            
            if (s[i-1] == "1" or (s[i-1] == "2" and s[i] in "0123456")):
                dp[i] += dp[i-2]

        return dp[n-1]