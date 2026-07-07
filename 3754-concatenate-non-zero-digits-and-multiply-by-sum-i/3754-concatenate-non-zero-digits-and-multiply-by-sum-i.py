class Solution:
    def sumAndMultiply(self, n: int) -> int:
        nums = str(n)
        x = ""
        total = 0
        for i in range(len(nums)):
            if nums[i] != "0":
                x += nums[i]
                total += int(nums[i])
        if x == "":
            return 0
        return int(x) * total