class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        dp = {}

        def dfs(i):
            if i == len(nums):
                return 0
            if i in dp:
                return dp[i]

            currSum = max(dfs(i+1), 0)
            dp[i] = currSum + nums[i]
            return dp[i]
        dfs(0)
        return max(dp.values())
