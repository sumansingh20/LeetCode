class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        arr = sorted((nums[i], i) for i in range(n))
        pos = [0] * n
        for i in range(n):
            pos[arr[i][1]] = i
        LOG = n.bit_length()
        up = [[0] * LOG for _ in range(n)]
        r = 0
        for i in range(n):
            r = max(r, i)
            while r + 1 < n and arr[r + 1][0] - arr[i][0] <= maxDiff and arr[r + 1][0] - arr[r][0] <= maxDiff:
                r += 1
            up[i][0] = r
        for j in range(1, LOG):
            for i in range(n):
                up[i][j] = up[up[i][j - 1]][j - 1]
        ans = []
        for u, v in queries:
            l, r = sorted((pos[u], pos[v]))
            if l == r:
                ans.append(0)
                continue
            cur = l
            step = 0
            for j in range(LOG - 1, -1, -1):
                if up[cur][j] < r:
                    cur = up[cur][j]
                    step += 1 << j
            ans.append(step + 1 if up[cur][0] >= r else -1)
        return ans



