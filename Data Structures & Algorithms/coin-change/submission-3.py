class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        if amount < min(coins) and amount != 0:
            return -1
        if amount < min(coins):
            return 0

        dp = [-1] * (amount + 1)
        dp[min(coins)] = 1
        dp[0] = 0
        for i in range(min(coins)+1, amount+1):

            for coin in coins:

                if i - coin >= 0 and dp[i-coin] != -1:

                    if dp[i] != -1:
                        dp[i] = min(dp[i], dp[i-coin])
                    else:
                        dp[i] = dp[i-coin]

            if dp[i] != -1:
                dp[i]+= 1

        print(dp)

        return dp[amount]