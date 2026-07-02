class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        q.append((0, 0))

        cost = [[1000000] * n for _ in range(m)]
        cost[0][0] = grid[0][0]

        d = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while q:
            x, y = q.popleft()
            for dx, dy in d:
                nx = x + dx
                ny = y + dy

                if nx >= 0 and nx < m and ny >= 0 and ny < n:
                    new = cost[x][y] + grid[nx][ny]
                    if new < cost[nx][ny]:
                        cost[nx][ny] = new

                        if grid[nx][ny] == 0:
                            q.appendleft((nx, ny))
                        else:
                            q.append((nx, ny))
        if cost[m - 1][n - 1] < health:
            return True
        return False


