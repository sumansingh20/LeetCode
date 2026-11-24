class Solution:
    def maxLength(self, nums: List[int]) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        n = len(nums)
        ans = 1
        for i in range(n):
            p = 1
            g = 0
            l = 1
            for j in range(i, n):
                x = nums[j]
                p *= x
                g = gcd(g, x)
                l = (l * x) // gcd(l, x)
                if p == g * l and j - i + 1 > ans:
                    ans = j - i + 1
        return ans