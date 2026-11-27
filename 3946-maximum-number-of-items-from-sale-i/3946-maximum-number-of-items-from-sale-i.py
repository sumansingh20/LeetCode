class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        max_f = 0
        min_p = items[0][1]
        for f, p in items:
            if f > max_f:
                max_f = f
            if p < min_p:
                min_p = p

        freq = [0] * (max_f + 1)
        for f, _ in items:
            freq[f] += 1

        mult = [0] * (max_f + 1)
        for f in range(1, max_f + 1):
            if freq[f] > 0:
                total = 0
                for m in range(f, max_f + 1, f):
                    total += freq[m]
                mult[f] = total

        dp = [0] * (budget + 1)
        for f, p in items:
            v = mult[f]
            for w in range(budget, p - 1, -1):
                cand = dp[w - p] + v
                if cand > dp[w]:
                    dp[w] = cand

        ans = 0
        for w in range(budget + 1):
            total = dp[w] + (budget - w) // min_p
            if total > ans:
                ans = total
        return ans