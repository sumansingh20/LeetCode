class Solution:
    def minimumDeletions(self, nums):
        n = len(nums)
        small = nums.index(min(nums))
        large = nums.index(max(nums))
        if small > large:
            small, large = large, small
        front = large + 1
        back = n - small
        both = small + 1 + n - large
        return min(front, back, both)