class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(i, total):
            if i >= len(nums):
                if total == target:
                    return 1
                else:
                    return 0

            if (i,total) in dp:
                return dp[(i, total)]

            sub = dfs(i+1, total - nums[i])

            add = dfs(i+1, total + nums[i])

            dp[(i,total)] = sub + add

            return dp[(i,total)]
        res = dfs(0,0)
        print(dp[(0,0)])
        return res
            