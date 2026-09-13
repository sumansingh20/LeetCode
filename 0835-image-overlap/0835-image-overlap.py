class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        a = []
        b = []
        for i in range(n):
            for j in range(n):
                if img1[i][j]:
                    a.append((i, j))
                if img2[i][j]:
                    b.append((i, j))
        count = {}
        ans = 0
        for x1, y1 in a:
            for x2, y2 in b:
                d = (x2 - x1, y2 - y1)
                if d in count:
                    count[d] += 1
                else:
                    count[d] = 1
                ans = max(ans, count[d])
        return ans