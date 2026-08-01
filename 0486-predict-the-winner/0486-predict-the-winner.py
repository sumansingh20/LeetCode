class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        dp = {}
        def dfs(i, j):
            if i == j:
                return nums[i]
            if (i, j) in dp:
                return dp[(i, j)]
            a = nums[i] - dfs(i + 1, j)
            b = nums[j] - dfs(i, j - 1)
            dp[(i, j)] = max(a, b)
            return dp[(i, j)]
        return dfs(0, len(nums) - 1) >= 0