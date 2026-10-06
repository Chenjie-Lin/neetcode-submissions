class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        dp = {}

        def dfs(i):
            if i == len(nums) - 1:
                return True
            if i in dp:
                return dp[i]
            dp[i] = False
            for j in range(1, nums[i]+ 1):
                dp[i] = dp[i] or dfs(i + j)
            return dp[i]
        
        return dfs(0)