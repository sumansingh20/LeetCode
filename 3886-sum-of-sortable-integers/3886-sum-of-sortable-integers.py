class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        divisors = []
        for i in range(1, n + 1):
            if i * i > n:
                break
            if n % i == 0:
                divisors.append(i)
                if i * i != n:
                    divisors.append(n // i)
        ans = 0
        for k in divisors:
            possible = True
            prev_max = -1
            for start in range(0, n, k):
                drops = 0
                if nums[start + k - 1] > nums[start]:
                    drops = drops + 1
                cur_min = nums[start]
                cur_max = nums[start]
                for j in range(start, start + k):
                    if nums[j] < cur_min:
                        cur_min = nums[j]
                    if nums[j] > cur_max:
                        cur_max = nums[j]
                    if j < start + k - 1 and nums[j] > nums[j + 1]:
                        drops = drops + 1
                if drops > 1:
                    possible = False
                    break
                if prev_max != -1 and prev_max > cur_min:
                    possible = False
                    break
                prev_max = cur_max
            if possible:
                ans = ans + k
        return ans