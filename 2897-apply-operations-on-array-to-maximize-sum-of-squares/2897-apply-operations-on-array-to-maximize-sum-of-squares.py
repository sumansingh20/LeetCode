class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        bit_counts = [0] * 32
        for num in nums:
            for i in range(32):
                if (num >> i) & 1:
                    bit_counts[i] += 1
        final_nums = [0] * k
        for i in range(k):
            current = 0
            for bit in range(31, -1, -1):
                if bit_counts[bit] > 0:
                    current += (1 << bit)
                    bit_counts[bit] -= 1
            final_nums[i] = current
        total_sum = 0
        mod = 10**9 + 7
        for num in final_nums:
            total_sum = (total_sum + num * num) % mod
        return total_sum