class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]):
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visit = [False] * n
        ans = 0
        def dfs(node):
            visit[node] = True
            nums.append(node)
            for nextNode in graph[node]:
                if not visit[nextNode]:
                    dfs(nextNode)
        for i in range(n):
            if not visit[i]:
                nums = []
                dfs(i)
                node = len(nums)
                edge = 0
                for x in nums:
                    edge += len(graph[x])
                edge //= 2
                if edge == node * (node - 1) // 2:
                    ans += 1
        return ans


        