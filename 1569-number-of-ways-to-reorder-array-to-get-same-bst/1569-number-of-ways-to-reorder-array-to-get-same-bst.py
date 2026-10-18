class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        mod = 1000000007
        n = len(nums)        
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i
        def comb(n, r):
            return fact[n] // (fact[r] * fact[n - r])
        def solve(arr):
            if len(arr) <= 2:
                return 1
            root = arr[0]
            left = []
            right = []
            for i in range(1, len(arr)):
                if arr[i] < root:
                    left.append(arr[i])
                else:
                    right.append(arr[i])
            ways = comb(len(left) + len(right), len(left))
            return (ways * solve(left) * solve(right)) % mod
        return (solve(nums) - 1) % mod