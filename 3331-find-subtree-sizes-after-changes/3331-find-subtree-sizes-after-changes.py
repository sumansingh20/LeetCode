class Solution:
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
        n = len(nums := parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        new_parent = parent[:]
        last_seen = [-1] * 26

        def dfs1(u: int) -> None:
            ch = ord(s[u]) - 97
            prev = last_seen[ch]
            if prev != -1 and u != 0:
                new_parent[u] = prev
            last_seen[ch] = u
            for v in children[u]:
                dfs1(v)
            last_seen[ch] = prev

        dfs1(0)

        tree = [[] for _ in range(n)]
        for i in range(1, n):
            tree[new_parent[i]].append(i)

        ans = [0] * n

        def dfs2(u: int) -> int:
            size = 1
            for v in tree[u]:
                size += dfs2(v)
            ans[u] = size
            return size

        dfs2(0)
        return ans