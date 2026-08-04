class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s = set(nums)
        start = min(nums)
        end = max(nums)
        ans = []
        for i in range(start, end + 1):
            if i not in s:
                ans.append(i)
        return ans