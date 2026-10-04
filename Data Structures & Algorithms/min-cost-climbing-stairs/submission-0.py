class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n+1)
        dp[1], dp[2] = cost[0], cost[1]
        for i in range(3,n+1):

            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2]+ cost[i-1]) 
        
        print(dp)

        return  min(dp[n], dp[n-1])