class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1
        half = [x // 2 for x in cnt]
        mid = ""
        for i in range(26):
            if cnt[i] % 2:
                mid = chr(i + 97)
                break
        def ways(arr, rem):
            ans = 1
            r = rem
            for x in arr:
                ans *= comb(r, x)
                if ans >= k:
                    return ans
                r -= x
            return ans
        total = sum(half)
        if ways(half, total) < k:
            return ""
        left = []
        for _ in range(total):
            for i in range(26):
                if half[i] == 0:
                    continue
                half[i] -= 1
                cnt_way = ways(half, total - 1)
                if cnt_way >= k:
                    left.append(chr(i + 97))
                    total -= 1
                    break
                k -= cnt_way
                half[i] += 1
        left = "".join(left)
        return left + mid + left[::-1]