class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        dist = [[-1] * n for _ in range(n)]
        queue = deque()

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    dist[row][col] = 0
                    queue.append((row, col))

        while queue:
            row, col = queue.popleft()

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[row][col] + 1
                    queue.append((nr, nc))

        heap = [(-dist[0][0], 0, 0)]
        visited = [[False] * n for _ in range(n)]

        while heap:
            safe, row, col = heappop(heap)
            safe = -safe

            if visited[row][col]:
                continue

            visited[row][col] = True

            if row == n - 1 and col == n - 1:
                return safe

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    next_safe = min(safe, dist[nr][nc])
                    heappush(heap, (-next_safe, nr, nc))

        return 0