class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3:
            return max(nums)
        dp1 = [0] * (n+1)
        dp2 = [0] * (n+1)

        dp1[1], dp1[2], dp1[3] = nums[0], nums[1], nums[0] + nums[2]
        dp2[2], dp2[3], dp2[4] = nums[1], nums[2], nums[1] + nums[3]
        for i in range(4, n):
            dp1[i] = max(dp1[i-2] + nums[i-1], dp1[i-3] + nums[i-1])
        
        for i in range(5, n+1):
            dp2[i] = max(dp2[i-2] + nums[i-1], dp2[i-3] + nums[i-1])

        return max(max(dp1), max(dp2))

        
        