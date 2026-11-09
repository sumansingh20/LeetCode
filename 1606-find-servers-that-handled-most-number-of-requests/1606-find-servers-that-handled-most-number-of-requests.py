class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        m = 1
        while m < k:
            m *= 2
        tree = [0] * (2 * m)
        for i in range(m + k, 2 * m):
            tree[i] = 10**18
        for i in range(m - 1, 0, -1):
            tree[i] = min(tree[2 * i], tree[2 * i + 1])
        cnt = [0] * k
        for i in range(len(arrival)):
            t = arrival[i]
            if tree[1] > t:
                continue
            p = m + (i % k)
            while tree[p] > t or p < m:
                if tree[p] <= t:
                    p = p * 2
                elif p % 2 == 0:
                    p += 1
                else:
                    p = (p + 1) // 2
            s = p - m
            cnt[s] += 1
            tree[p] = t + load[i]
            while p > 1:
                p = p // 2
                tree[p] = min(tree[2 * p], tree[2 * p + 1])
        mx = max(cnt)
        ans = []
        for i in range(k):
            if cnt[i] == mx:
                ans.append(i)
        return ans