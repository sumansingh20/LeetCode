class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k
        for x in nums:
            x %= k
            ndp = [0] * k
            ndp[x] += 1
            for r in range(k):
                if dp[r]:
                    nr = (r * x) % k
                    ndp[nr] += dp[r]
            for r in range(k):
                ans[r] += ndp[r]
            dp = ndp
        return ans