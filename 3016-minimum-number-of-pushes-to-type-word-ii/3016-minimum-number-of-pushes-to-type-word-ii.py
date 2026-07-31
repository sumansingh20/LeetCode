class Solution:
    def minimumPushes(self, word: str) -> int:
        cnt = {}
        for ch in word:
            if ch in cnt:
                cnt[ch] += 1
            else:
                cnt[ch] = 1
        arr = sorted(cnt.values(), reverse=True)
        ans = 0
        for i in range(len(arr)):
            ans += arr[i] * (i // 8 + 1)
        return ans