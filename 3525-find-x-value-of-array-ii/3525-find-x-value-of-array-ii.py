class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        tree = [None] * (4 * n)
        def make(x):
            p = x % k
            cnt = [0] * k
            cnt[p] = 1
            return p, cnt
        def merge(left, right):
            p1, c1 = left
            p2, c2 = right
            cnt = c1[:]
            for r in range(k):
                new_r = (p1 * r) % k
                cnt[new_r] += c2[r]
            return (p1 * p2) % k, cnt
        def build(node, l, r):
            if l == r:
                tree[node] = make(nums[l])
                return
            mid = (l + r) // 2
            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)
            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])
        def update(node, l, r, pos, value):
            if l == r:
                tree[node] = make(value)
                return
            mid = (l + r) // 2
            if pos <= mid:
                update(node * 2, l, mid, pos, value)
            else:
                update(node * 2 + 1, mid + 1, r, pos, value)
            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])
        def query(node, l, r, start):
            if l >= start:
                return tree[node]
            mid = (l + r) // 2
            if start > mid:
                return query(node * 2 + 1, mid + 1, r, start)
            left = query(node * 2, l, mid, start)
            right = query(node * 2 + 1, mid + 1, r, start)
            return merge(left, right)
        build(1, 0, n - 1)
        ans = []
        for index, value, start, x in queries:
            nums[index] = value
            update(1, 0, n - 1, index, value)
            product, count = query(1, 0, n - 1, start)
            ans.append(count[x])
        return ans