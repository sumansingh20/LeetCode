class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            sum[i] = sum[i + 1] + piles[i]
        dp = [[0] * (n + 1) for i in range(n)]
        for i in range(n - 1, -1, -1):
            for m in range(1, n + 1):
                if i + 2 * m >= n:
                    dp[i][m] = sum[i]
                else:
                    ans = 0
                    for x in range(1, 2 * m + 1):
                        value = sum[i] - dp[i + x][max(m, x)]
                        if value > ans:
                            ans = value
                    dp[i][m] = ans
        return dp[0][1]
        