class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        a = []
        for i in range(n):
            x = nums[i]
            s = 0
            while x > 0:
                s = s + (x % 10)
                x = x // 10
            a.append([s, nums[i]])
        a.sort()
        b = []
        for i in range(n):
            b.append(a[i][1])
        pos = {}
        for i in range(n):
            pos[nums[i]] = i
        ans = 0
        for i in range(n):
            if nums[i] != b[i]:
                ans = ans + 1
                j = pos[b[i]]
                pos[nums[i]] = j
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
        return ans