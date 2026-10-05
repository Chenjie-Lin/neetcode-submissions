class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = {}

        def dfs(i, total):
            if total == amount:
                return 1
            if total > amount:
                return 0
            if i >= len(coins):
                return 0
            if (i,total) in dp:
                return dp[(i,total)]
            pick = dfs(i, total + coins[i])
            notpick = dfs(i+1, total)
            dp[(i,total)] = pick + notpick
            return dp[(i,total)]
        

        return dfs(0,0)