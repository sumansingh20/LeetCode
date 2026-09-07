class Solution:
    def distinctSubseqII(self, s: str) -> int:
        mod = 10**9 + 7
        dp = 0
        last = [0] * 26
        for ch in s:
            x = ord(ch) - 97
            new = dp + 1
            dp = (dp + new - last[x]) % mod
            last[x] = new
        return dp