class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        count = {}
        left = 0
        ans = 0
        for right in range(len(nums)):
            num = nums[right]
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
            while count[num] > k:
                count[nums[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans