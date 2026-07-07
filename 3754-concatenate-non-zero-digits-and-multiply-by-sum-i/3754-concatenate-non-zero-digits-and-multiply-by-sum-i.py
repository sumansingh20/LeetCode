class Solution:
    def sumAndMultiply(self, n: int) -> int:
        nums = str(n)
        x = 0
        total = 0
        for i in range(len(nums)):
            if nums[i] != "0":
                x = x * 10 + int(nums[i])
                total += int(nums[i])
        return x * total