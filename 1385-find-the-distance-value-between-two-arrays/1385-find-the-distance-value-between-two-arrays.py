class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        ans = 0
        for x in arr1:
            ok = True
            for y in arr2:
                if abs(x - y) <= d:
                    ok = False
                    break
            if ok:
                ans = ans + 1
        return ans