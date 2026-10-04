class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        
        for i in range(min(coins), amount+1):

            for coin in coins:

                if i - coin >= 0:

                    dp[i] = min(dp[i], dp[i-coin])

            if dp[i] != -1:
                dp[i]+= 1


        return dp[amount] if dp[amount] != float("inf") else -1