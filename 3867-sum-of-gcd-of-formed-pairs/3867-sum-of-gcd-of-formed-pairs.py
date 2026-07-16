class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        arr = []
        mx = 0
        for x in nums:
            if x > mx:
                mx = x
            arr.append(gcd(x, mx))
        arr.sort()
        ans = 0
        i = 0
        j = len(arr) - 1
        while i < j:
            ans += gcd(arr[i], arr[j])
            i += 1
            j -= 1
        return ans