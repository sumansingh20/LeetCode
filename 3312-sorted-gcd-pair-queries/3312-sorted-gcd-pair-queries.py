class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        m = max(nums)
        c = [0] * (m + 1)
        for n in nums:
            c[n] += 1
            
        p = [0] * (m + 1)
        for i in range(1, m + 1):
            t = sum(c[i::i])
            p[i] = t * (t - 1) // 2
            
        for i in range(m, 0, -1):
            for j in range(2 * i, m + 1, i):
                p[i] -= p[j]
                
        for i in range(1, m + 1):
            p[i] += p[i - 1]
            
        o = []
        for q in queries:
            l, r = 1, m
            while l < r:
                md = (l + r) // 2
                if p[md] <= q:
                    l = md + 1
                else:
                    r = md
            o.append(l)
        return o