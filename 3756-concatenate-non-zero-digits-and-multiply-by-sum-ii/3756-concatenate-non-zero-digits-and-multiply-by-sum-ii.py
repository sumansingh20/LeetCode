class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        mod = 1000000007

        pos = []
        nums = []

        for i in range(len(s)):
            if s[i] != "0":
                pos.append(i)
                nums.append(int(s[i]))

        n = len(nums)

        preSum = [0] * (n + 1)
        preNum = [0] * (n + 1)
        power = [1] * (n + 1)

        for i in range(n):
            preSum[i + 1] = preSum[i] + nums[i]
            preNum[i + 1] = (preNum[i] * 10 + nums[i]) % mod
            power[i + 1] = (power[i] * 10) % mod

        ans = []

        for l, r in queries:

            left = 0
            right = n - 1

            while left <= right:
                mid = (left + right) // 2
                if pos[mid] >= l:
                    right = mid - 1
                else:
                    left = mid + 1

            start = left

            left = 0
            right = n - 1

            while left <= right:
                mid = (left + right) // 2
                if pos[mid] <= r:
                    left = mid + 1
                else:
                    right = mid - 1

            end = right

            if start > end:
                ans.append(0)
                continue

            length = end - start + 1
            number = (preNum[end + 1] - preNum[start] * power[length]) % mod
            total = preSum[end + 1] - preSum[start]

            ans.append((number * total) % mod)

        return ans