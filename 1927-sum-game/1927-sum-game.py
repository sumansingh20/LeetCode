class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        left = 0
        right = 0
        a = 0
        b = 0
        for i in range(half):
            if num[i] == "?":
                a += 1
            else:
                left += int(num[i])
        for i in range(half, n):
            if num[i] == "?":
                b += 1
            else:
                right += int(num[i])
        if (a + b) % 2 == 1:
            return True
        diff = left - right
        need = (b - a) // 2 * 9
        return diff != need