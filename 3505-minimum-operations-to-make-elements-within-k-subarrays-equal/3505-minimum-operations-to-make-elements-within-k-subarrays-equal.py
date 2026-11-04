class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        l = []
        r = []
        pos = [0] * n
        lsum = 0
        rsum = 0
        lcnt = 0
        rcnt = 0
        c = [0] * (n + 1)
        
        for i in range(n):
            if i >= x:
                old = i - x
                if pos[old] == 1:
                    lsum = lsum - nums[old]
                    lcnt = lcnt - 1
                else:
                    rsum = rsum - nums[old]
                    rcnt = rcnt - 1
                    
            while r and r[0][1] <= i - x:
                heapq.heappop(r)
                
            if not r or nums[i] <= r[0][0]:
                heapq.heappush(l, (-nums[i], i))
                pos[i] = 1
                lsum = lsum + nums[i]
                lcnt = lcnt + 1
            else:
                heapq.heappush(r, (nums[i], i))
                pos[i] = 2
                rsum = rsum + nums[i]
                rcnt = rcnt + 1
                
            while lcnt > rcnt + 1:
                while l[0][1] <= i - x:
                    heapq.heappop(l)
                val, idx = heapq.heappop(l)
                val = -val
                lsum = lsum - val
                lcnt = lcnt - 1
                pos[idx] = 2
                rsum = rsum + val
                rcnt = rcnt + 1
                heapq.heappush(r, (val, idx))
                
            while lcnt < rcnt:
                while r[0][1] <= i - x:
                    heapq.heappop(r)
                val, idx = heapq.heappop(r)
                rsum = rsum - val
                rcnt = rcnt - 1
                pos[idx] = 1
                lsum = lsum + val
                lcnt = lcnt + 1
                heapq.heappush(l, (-val, idx))
                
            if i >= x - 1:
                while l[0][1] <= i - x:
                    heapq.heappop(l)
                med = -l[0][0]
                c[i + 1] = med * lcnt - lsum + rsum - med * rcnt
                
        inf = 10 ** 18
        dp = [0] * (n + 1)
        
        for t in range(1, k + 1):
            ndp = [inf] * (n + 1)
            for i in range(t * x, n + 1):
                ndp[i] = ndp[i - 1]
                if dp[i - x] + c[i] < ndp[i]:
                    ndp[i] = dp[i - x] + c[i]
            dp = ndp
        return dp[n]