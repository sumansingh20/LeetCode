class Solution:
    def removeCoveredIntervals(self, nums: List[List[int]]):
        nums.sort(key=lambda arr: (arr[0], -arr[1]))
        ans = 0
        end = -1
        for i in range(len(nums)):
            if nums[i][1] > end:
                ans += 1
                end = nums[i][1]
        return ans

        