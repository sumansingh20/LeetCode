class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        nums = sorted(set(arr))
        rank = {}
        for i in range(len(nums)):
            rank[nums[i]] = i + 1
        for i in range(len(arr)):
            arr[i] = rank[arr[i]]
        return arr


        