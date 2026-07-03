class Solution:
    def findMaxPathScore(self, edges: list[list[int]], online: list[bool], k: int) -> int:
        n = len(online)
        adj = [[] for _ in range(n)]
        indeg = [0] * n
        weights = set()

        for u, v, w in edges:
            if online[u] and online[v]:
                adj[u].append((v, w))
                indeg[v] += 1
                weights.add(w)
        if not weights:
            return -1
        q = deque([i for i in range(n) if online[i] and indeg[i] == 0])
        topo = []
        while q:
            u = q.popleft()
            topo.append(u)
            for v, _ in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        W = sorted(list(weights))
        ans = -1
        l, r = 0, len(W) - 1
        while l <= r:
            mid = (l + r) // 2
            target = W[mid]
            dist = [float('inf')] * n
            dist[0] = 0
            for u in topo:
                if dist[u] == float('inf'):
                    continue
                for v, w in adj[u]:
                    if w >= target and dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
            if dist[n - 1] <= k:
                ans = target
                l = mid + 1
            else:
                r = mid - 1
        return ans