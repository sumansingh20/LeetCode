class Solution:
    def singleNumber(self, nums: List[int]):
        ans = 0
        for num in nums:
            ans ^= num
        return ans
        