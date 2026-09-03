class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        x = min(nums1)
        for n in nums1:
            if n % 2 != x % 2 and n < x:
                return False
        if x % 2 == 0:
            for n in nums1:
                if n % 2:
                    return False
        return True