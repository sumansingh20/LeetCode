class Solution:
    def minMoves(self, nums: list[int]) -> int:
        m = min(nums)
        ans = 0
        for x in nums:
            ans = ans + (x - m)
        return ans