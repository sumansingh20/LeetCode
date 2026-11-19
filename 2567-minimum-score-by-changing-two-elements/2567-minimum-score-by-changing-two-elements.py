class Solution:
    def minimizeSum(self, nums: list[int]) -> int:
        nums.sort()
        first = nums[-1] - nums[2]
        second = nums[-2] - nums[1]
        third = nums[-3] - nums[0]
        return min(first, second, third)