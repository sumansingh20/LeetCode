class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        nxt = [{}]
        link = [-1]
        length = [0]
        cnt = [0]
        last = 0

        for x in nums:
            cur = len(nxt)
            nxt.append({})
            link.append(0)
            length.append(length[last] + 1)
            cnt.append(1)

            p = last
            while p != -1 and x not in nxt[p]:
                nxt[p][x] = cur
                p = link[p]

            if p == -1:
                link[cur] = 0
            else:
                q = nxt[p][x]
                if length[p] + 1 == length[q]:
                    link[cur] = q
                else:
                    clone = len(nxt)
                    nxt.append(nxt[q].copy())
                    link.append(link[q])
                    length.append(length[p] + 1)
                    cnt.append(0)
                    while p != -1 and nxt[p].get(x) == q:
                        nxt[p][x] = clone
                        p = link[p]
                    link[q] = clone
                    link[cur] = clone
            last = cur

        size = len(nxt)
        buckets = [[] for _ in range(n + 1)]
        for i in range(1, size):
            buckets[length[i]].append(i)

        for l in range(n, 0, -1):
            for u in buckets[l]:
                cnt[link[u]] += cnt[u]

        ans = n
        for i in range(1, size):
            if cnt[i] == 1:
                val = length[link[i]] + 1
                if val < ans:
                    ans = val

        return ans