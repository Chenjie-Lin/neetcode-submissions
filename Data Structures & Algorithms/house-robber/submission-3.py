class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n+1)
        if n <= 2:
            return max(nums)
        dp[1], dp[2], dp[3] = nums[0], nums[1], nums[0] + nums[2]

        for i in range(4, n+1):
            dp[i] = max(dp[i-2] + nums[i-1], dp[i-3] + nums[i-1])
        
        return max(dp)