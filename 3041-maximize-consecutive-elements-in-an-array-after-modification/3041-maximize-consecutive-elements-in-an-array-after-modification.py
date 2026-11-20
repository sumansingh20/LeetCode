class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        streak = {}
        best = 0
        for num in nums:
            streak[num + 1] = streak.get(num, 0) + 1
            streak[num] = streak.get(num - 1, 0) + 1
            best = max(best, streak[num + 1], streak[num])
        return best