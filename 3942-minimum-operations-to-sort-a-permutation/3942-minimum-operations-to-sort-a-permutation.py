class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        is_inc = True
        is_dec = True
        for i in range(n):
            if nums[(i + 1) % n] != (nums[i] + 1) % n:
                is_inc = False
            if nums[(i + 1) % n] != (nums[i] - 1) % n:
                is_dec = False
        if not is_inc and not is_dec:
            return -1
        k = 0
        for i in range(n):
            if nums[i] == 0:
                k = i
                break
        ans = n + 5
        if is_inc:
            cost = min(k, n - k + 2)
            if cost < ans:
                ans = cost
        if is_dec:
            cost = min(n - k, (k + 1) % n + 1)
            if cost < ans:
                ans = cost
        return ans