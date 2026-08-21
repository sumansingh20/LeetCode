class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        def count(x):
            ans = 0
            n = len(coins)
            for mask in range(1, 1 << n):
                lcm = 1
                bits = 0
                for i in range(n):
                    if mask >> i & 1:
                        bits += 1
                        lcm = lcm * coins[i] // gcd(lcm, coins[i])
                if bits % 2:
                    ans += x // lcm
                else:
                    ans -= x // lcm
            return ans
        low, high = 1, min(coins) * k
        while low < high:
            mid = (low + high) // 2
            if count(mid) >= k:
                high = mid
            else:
                low = mid + 1
        return low