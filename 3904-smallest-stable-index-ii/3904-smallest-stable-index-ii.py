class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        right = [0] * n
        right[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            right[i] = min(right[i + 1], nums[i])
        mx = nums[0]
        for i in range(n):
            mx = max(mx, nums[i])
            if mx - right[i] <= k:
                return i
        return -1