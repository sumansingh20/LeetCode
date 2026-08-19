class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = {}
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                if row not in rows:
                    rows[row] = set()
                rows[row].add(seat)
        ans = (n - len(rows)) * 2
        for row in rows:
            seats = rows[row]
            left = True
            middle = True
            right = True
            for seat in range(2, 6):
                if seat in seats:
                    left = False
            for seat in range(4, 8):
                if seat in seats:
                    middle = False
            for seat in range(6, 10):
                if seat in seats:
                    right = False
            if left and right:
                ans += 2
            elif left or middle or right:
                ans += 1
        return ans