import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        g = []
        for i in range(n):
            g.append([])
        for e in edges:
            u = e[0]
            v = e[1]
            w = e[2]
            g[u].append((v, w))
        vis = [k + 1] * n
        q = [(0, 0, 1)]
        while q:
            d, u, c = heapq.heappop(q)
            if u == n - 1:
                return d
            if c >= vis[u]:
                continue
            vis[u] = c
            for v, w in g[u]:
                if labels[v] == labels[u]:
                    nc = c + 1
                else:
                    nc = 1
                if nc <= k and nc < vis[v]:
                    heapq.heappush(q, (d + w, v, nc))   
        return -1