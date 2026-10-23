class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        ans = None
        for i in range(len(nums)):
            if nums[i] != i:
                if ans is None:
                    ans = nums[i]
                else:
                    ans = ans & nums[i]
        if ans is None:
            return 0
        return ans