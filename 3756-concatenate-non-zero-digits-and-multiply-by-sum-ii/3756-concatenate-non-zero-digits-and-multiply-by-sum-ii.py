import bisect

class Solution:
    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        mod = 1000000007
        
        pos = []
        val = []
        for i in range(len(s)):
            if s[i] != '0':
                pos.append(i)
                val.append(int(s[i]))
                
        k = len(val)
        
        p_sum = [0] * (k + 1)
        p_val = [0] * (k + 1)
        p_10 = [1] * (k + 1)
        
        for i in range(k):
            p_sum[i + 1] = p_sum[i] + val[i]
            p_val[i + 1] = (p_val[i] * 10 + val[i]) % mod
            p_10[i + 1] = (p_10[i] * 10) % mod
            
        ans = []
        
        for l, r in queries:
            left_idx = bisect.bisect_left(pos, l)
            right_idx = bisect.bisect_right(pos, r) - 1
            
            if left_idx <= right_idx:
                length = right_idx - left_idx + 1
                
                num = (p_val[right_idx + 1] - p_val[left_idx] * p_10[length]) % mod
                total = p_sum[right_idx + 1] - p_sum[left_idx]
                
                ans.append((num * total) % mod)
            else:
                ans.append(0)
                
        return ans