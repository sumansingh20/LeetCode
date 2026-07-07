class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        nums = []
        total = 0
        while n > 0:
            digit = n % 10
            if digit != 0:
                nums.append(digit)
                total += digit
            n //= 10
        x = 0
        for i in range(len(nums) - 1, -1, -1):
            x = x * 10 + nums[i]
        return x * total