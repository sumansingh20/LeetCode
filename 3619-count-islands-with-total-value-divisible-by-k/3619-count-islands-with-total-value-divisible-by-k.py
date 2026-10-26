class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    total = 0
                    stack = [(i, j)]
                    
                    while stack:
                        r, c = stack.pop()
                        if r < 0 or r >= m or c < 0 or c >= n:
                            continue
                        if grid[r][c] == 0:
                            continue
                        total = total + grid[r][c]
                        grid[r][c] = 0
                        stack.append((r - 1, c))
                        stack.append((r + 1, c))
                        stack.append((r, c - 1))
                        stack.append((r, c + 1))
                    if total % k == 0:
                        count = count + 1    
        return count