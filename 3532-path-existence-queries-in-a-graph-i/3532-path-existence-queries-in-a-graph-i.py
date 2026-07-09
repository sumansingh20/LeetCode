class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        group = [0] * n
        group[0] = 1
        for i in range(1, n):
            if nums[i] - nums[i - 1] <= maxDiff:
                group[i] = group[i - 1]
            else:
                group[i] = group[i - 1] + 1
        ans = []
        for q in queries:
            u = q[0]
            v = q[1]
            if group[u] == group[v]:
                ans.append(True)
            else:
                ans.append(False)
        return ans