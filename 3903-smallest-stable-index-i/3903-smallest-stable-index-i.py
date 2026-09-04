class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        suf = [0] * n
        suf[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suf[i] = min(nums[i], suf[i + 1])
        mx = 0
        for i in range(n):
            mx = max(mx, nums[i])
            if mx - suf[i] <= k:
                return i
        return -1