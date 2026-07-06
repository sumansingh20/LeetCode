class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        zero = s.count("0")
        if zero == 0:
            return 0
        parent = list(range(n + 3))
        dist = [-1] * (n + 1)
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        queue = deque([zero])
        dist[zero] = 0
        parent[zero] = find(zero + 2)
        while queue:
            current = queue.popleft()
            low = max(0, k - (n - current))
            high = min(k, current)
            left = current + k - 2 * high
            right = current + k - 2 * low
            value = find(left)
            while value <= right:
                dist[value] = dist[current] + 1
                if value == 0:
                    return dist[value]
                queue.append(value)
                parent[value] = find(value + 2)
                value = find(value)
        return -1