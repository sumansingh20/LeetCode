class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        count = [0] * 26
        for ch in s:
            count[ord(ch) - 97] += 1

        odd = 0
        middle = ""

        for i in range(26):
            if count[i] % 2:
                odd += 1
                middle = chr(i + 97)

        if odd > 1:
            return ""

        half = [x // 2 for x in count]
        m = len(s) // 2
        ans = []

        for i in range(m):
            x = ord(target[i]) - 97

            if half[x] > 0:
                half[x] -= 1
                ans.append(target[i])
            else:
                break
        else:
            left = "".join(ans)
            pal = left + middle + left[::-1]

            if pal > target:
                return pal

            i = m

        while True:
            for c in range(ord(target[i]) - 96, 26):
                if half[c] > 0:
                    half[c] -= 1
                    ans.append(chr(c + 97))

                    for j in range(26):
                        ans += [chr(j + 97)] * half[j]

                    left = "".join(ans)
                    return left + middle + left[::-1]

            if not ans:
                return ""

            i -= 1
            x = ord(ans.pop()) - 97
            half[x] += 1