class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        if grid[0][0] == ')' or grid[m-1][n-1] == '(':
            return False
        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(1)
        for i in range(m):
            for j in range(n):
                for x in dp[i][j]:
                    if i + 1 < m:
                        v = x + (1 if grid[i+1][j] == '(' else -1)
                        if v >= 0:
                            dp[i+1][j].add(v)
                    if j + 1 < n:
                        v = x + (1 if grid[i][j+1] == '(' else -1)
                        if v >= 0:
                            dp[i][j+1].add(v)
        return 0 in dp[m-1][n-1]