class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(n):
            if dp[i] == float('inf'):
                continue
            for j in range(i + 1, min(i + 4, n + 1)):
                cost = dp[i] + costs[j - 1] + (j - i) ** 2
                if cost < dp[j]:
                    dp[j] = cost
        return dp[n]