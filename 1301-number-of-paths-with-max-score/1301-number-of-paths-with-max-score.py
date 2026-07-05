class Solution:
    def pathsWithMaxScore(self, board: list[str]) -> list[int]:
        n = len(board)
        mod = 1000000007
        dp = [[[-1, 0] for j in range(n)] for i in range(n)]
        dp[n - 1][n - 1] = [0, 1]
        move = [(-1, 0), (0, -1), (-1, -1)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == "X" or dp[i][j][1] == 0:
                    continue
                for x, y in move:
                    ni = i + x
                    nj = j + y
                    if 0 <= ni < n and 0 <= nj < n and board[ni][nj] != "X":
                        add = 0
                        if board[ni][nj] != "S" and board[ni][nj] != "E":
                            add = int(board[ni][nj])
                        total = dp[i][j][0] + add
                        if total > dp[ni][nj][0]:
                            dp[ni][nj][0] = total
                            dp[ni][nj][1] = dp[i][j][1]
                        elif total == dp[ni][nj][0]:
                            dp[ni][nj][1] = (dp[ni][nj][1] + dp[i][j][1]) % mod
        if dp[0][0][1] == 0:
            return [0, 0]
        return dp[0][0]