
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        mod = 1000000007

        tree1 = [0] * (n + 2)
        tree2 = [0] * (n + 2)
        last = {}

        cur = 0
        ans = 0

        for i in range(1, n + 1):
            x = nums[i - 1]

            if x in last:
                left = last[x] + 1
            else:
                left = 1

            last[x] = i

            sum1 = 0
            sum2 = 0
            j = i

            while j > 0:
                sum1 += tree1[j]
                sum2 += tree2[j]
                j -= j & -j

            total1 = (i + 1) * sum1 - sum2

            sum1 = 0
            sum2 = 0
            j = left - 1

            while j > 0:
                sum1 += tree1[j]
                sum2 += tree2[j]
                j -= j & -j

            total2 = left * sum1 - sum2
            add = total1 - total2
            cur = (cur + 2 * add + (i - left + 1)) % mod
            ans = (ans + cur) % mod
            j = left
            while j <= n + 1:
                tree1[j] += 1
                tree2[j] += left
                j += j & -j
            j = i + 1
            while j <= n + 1:
                tree1[j] -= 1
                tree2[j] -= i + 1
                j += j & -j
        return ans