class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        ans = [0]
        for i in range(1, n+1):
            offset = i % 2
            offset2 = i >> 1
            dp[i] = dp[offset2] + offset
        
        return dp