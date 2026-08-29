class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        a = sorted((x, i) for i, x in enumerate(nums))
        ans = nums[:]
        start = 0
        for i in range(1, len(a) + 1):
            if i == len(a) or a[i][0] - a[i - 1][0] > limit:
                group = a[start:i]
                pos = sorted(x[1] for x in group)
                val = [x[0] for x in group]
                for j in range(len(group)):
                    ans[pos[j]] = val[j]
                start = i
        return ans