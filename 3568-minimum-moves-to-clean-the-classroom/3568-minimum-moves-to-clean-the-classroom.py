class Solution:
    def minMoves(self, classroom, energy):
        m = len(classroom)
        n = len(classroom[0])
        litter = {}
        k = 0

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    sx, sy = i, j
                elif classroom[i][j] == 'L':
                    litter[(i, j)] = k
                    k += 1

        all_litter = (1 << k) - 1
        q = [(sx, sy, 0, energy, 0)]
        seen = {}
        p = 0

        while p < len(q):
            x, y, mask, e, moves = q[p]
            p += 1

            if mask == all_litter:
                return moves

            if seen.get((x, y, mask), -1) >= e:
                continue

            seen[(x, y, mask)] = e

            if e == 0:
                continue

            for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
                a = x + dx
                b = y + dy

                if 0 <= a < m and 0 <= b < n and classroom[a][b] != 'X':
                    ne = e - 1
                    nm = mask

                    if classroom[a][b] == 'R':
                        ne = energy

                    if (a, b) in litter:
                        nm |= 1 << litter[(a, b)]

                    q.append((a, b, nm, ne, moves + 1))

        return -1