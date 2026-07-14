class Solution:
    def subsequencePairCount(self, nums: List[int]):
        mod = 1000000007
        memo = {}
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        def solve(i, a, b):
            if i == len(nums):
                if a == b and a != 0:
                    return 1
                return 0
            if (i, a, b) in memo:
                return memo[(i, a, b)]
            x = solve(i + 1, a, b)
            if a == 0:
                x += solve(i + 1, nums[i], b)
            else:
                x += solve(i + 1, gcd(a, nums[i]), b)
            if b == 0:
                x += solve(i + 1, a, nums[i])
            else:
                x += solve(i + 1, a, gcd(b, nums[i]))
            memo[(i, a, b)] = x % mod
            return memo[(i, a, b)]
        return solve(0, 0, 0)