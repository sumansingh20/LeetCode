class Solution:
    def minScore(self, n: int, roads: List[List[int]]):
        graph = {i: [] for i in range(1, n + 1)}
        for u, v, dis in roads:
            graph[u].append((v, dis))
            graph[v].append((u, dis))
        visit = set()
        visit.add(1)
        q = deque([1])
        ans = float("inf")
        while q:
            node = q.popleft()
            for nei, dis in graph[node]:
                ans = min(ans, dis)
                if nei not in visit:
                    visit.add(nei)
                    q.append(nei)
        return ans