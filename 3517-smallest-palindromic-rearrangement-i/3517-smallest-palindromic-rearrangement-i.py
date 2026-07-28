class Solution:
    def smallestPalindrome(self, s: str):
        cnt = {}
        for ch in s:
            if ch in cnt:
                cnt[ch] += 1
            else:
                cnt[ch] = 1
        left = ""
        mid = ""
        for ch in sorted(cnt):
            left += ch * (cnt[ch] // 2)
            if cnt[ch] % 2 == 1:
                mid = ch
        right = left[::-1]
        return left + mid + right