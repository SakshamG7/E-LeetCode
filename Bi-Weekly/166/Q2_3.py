class Solution:
    def climbStairs(self, n: int, costs) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            cost_to_land = costs[i - 1]
            
            if i - 1 >= 0:
                total_cost = dp[i - 1] + cost_to_land + 1
                dp[i] = min(dp[i], total_cost)

            if i - 2 >= 0:
                total_cost = dp[i - 2] + cost_to_land + 4
                dp[i] = min(dp[i], total_cost)

            if i - 3 >= 0:
                total_cost = dp[i - 3] + cost_to_land + 9
                dp[i] = min(dp[i], total_cost)
        return dp[n]