class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
                
        res = [x for x in nums if x != 0]
        res.extend([0] * (len(nums) - len(res)))
        return res