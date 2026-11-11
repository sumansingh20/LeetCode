class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        ans = float('inf')        
        candidates = [0, need1, need2, max(need1, need2)]
        if costBoth < cost1 + cost2:
            candidates.append(max(need1, need2))
        for i in candidates:
            if i >= 0:
                c1 = max(0, need1 - i)
                c2 = max(0, need2 - i)
                cost = i * costBoth + c1 * cost1 + c2 * cost2
                if cost < ans:
                    ans = cost
        i = min(need1, need2)
        c1 = max(0, need1 - i)
        c2 = max(0, need2 - i)
        cost = i * costBoth + c1 * cost1 + c2 * cost2
        if cost < ans:
            ans = cost
        return ans