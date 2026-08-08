from functools import lru_cache

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        need = [0, 0, 0, 0]
        primes = [2, 3, 5, 7]

        for i in range(4):
            while t % primes[i] == 0:
                need[i] += 1
                t //= primes[i]

        if t != 1:
            return "-1"

        value = [
            (0, 0, 0, 0),
            (0, 0, 0, 0),
            (1, 0, 0, 0),
            (0, 1, 0, 0),
            (2, 0, 0, 0),
            (0, 0, 1, 0),
            (1, 1, 0, 0),
            (0, 0, 0, 1),
            (3, 0, 0, 0),
            (0, 2, 0, 0)
        ]

        @lru_cache(None)
        def count(a, b):
            if a == 0 and b == 0:
                return 0

            ans = 100

            for d in range(2, 10):
                x = max(0, a - value[d][0])
                y = max(0, b - value[d][1])

                if x == a and y == b:
                    continue

                ans = min(ans, 1 + count(x, y))

            return ans

        def possible(a, left):
            return (
                count(a[0], a[1])
                + a[2]
                + a[3]
                <= left
            )

        def make(a, size):
            ans = ""

            for i in range(size):
                left = size - i - 1

                for d in range(1, 10):
                    b = []

                    for j in range(4):
                        b.append(max(0, a[j] - value[d][j]))

                    if possible(b, left):
                        ans += str(d)
                        a = b
                        break

            return ans

        n = len(num)

        pref = [[0, 0, 0, 0] for _ in range(n + 1)]

        first_zero = -1

        for i in range(n):
            pref[i + 1] = pref[i][:]

            d = int(num[i])

            if d == 0:
                if first_zero == -1:
                    first_zero = i
            else:
                for j in range(4):
                    pref[i + 1][j] += value[d][j]

        if first_zero == -1:
            ok = True

            for i in range(4):
                if pref[n][i] < need[i]:
                    ok = False

            if ok:
                return num

        if first_zero == -1:
            start = n - 1
        else:
            start = first_zero

        for i in range(start, -1, -1):
            d = int(num[i])

            for x in range(d + 1, 10):
                a = []

                for j in range(4):
                    left = need[j]
                    left -= pref[i][j]
                    left -= value[x][j]

                    a.append(max(0, left))

                size = n - i - 1

                if possible(a, size):
                    ans = num[:i]
                    ans += str(x)
                    ans += make(a, size)

                    return ans

        minimum = count(need[0], need[1])
        minimum += need[2]
        minimum += need[3]

        size = max(n + 1, minimum)

        return make(need[:], size)