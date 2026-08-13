class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        s = list(s)
        n = len(s)
        tree = [0] * (4 * n)
        left = [0] * (4 * n)
        right = [0] * (4 * n)
        def build(node, l, r):
            if l == r:
                tree[node] = left[node] = right[node] = 1
                return
            mid = (l + r) // 2
            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)
            pull(node, l, r)
        def pull(node, l, r):
            mid = (l + r) // 2
            a = node * 2
            b = a + 1
            tree[node] = max(tree[a], tree[b])
            left[node] = left[a]
            right[node] = right[b]
            if s[mid] == s[mid + 1]:
                tree[node] = max(tree[node], right[a] + left[b])
                if left[a] == mid - l + 1:
                    left[node] += left[b]
                if right[b] == r - mid:
                    right[node] += right[a]
        def update(node, l, r, index):
            if l == r:
                return
            mid = (l + r) // 2
            if index <= mid:
                update(node * 2, l, mid, index)
            else:
                update(node * 2 + 1, mid + 1, r, index)
            pull(node, l, r)
        build(1, 0, n - 1)
        ans = []
        for i in range(len(queryIndices)):
            index = queryIndices[i]
            s[index] = queryCharacters[i]
            update(1, 0, n - 1, index)
            ans.append(tree[1])
        return ans