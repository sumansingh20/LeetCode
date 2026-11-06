class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        arr = []
        for l in logs:
            arr.append([l[1], l[0]])
        arr.sort()
        q = []
        for i in range(len(queries)):
            q.append([queries[i], i])
        q.sort()
        cnt = [0] * (n + 1)
        ans = [0] * len(queries)
        active = 0
        left = 0
        right = 0
        m = len(arr)
        
        for val, idx in q:
            while right < m and arr[right][0] <= val:
                s = arr[right][1]
                if cnt[s] == 0:
                    active = active + 1
                cnt[s] = cnt[s] + 1
                right = right + 1
            while left < m and arr[left][0] < val - x:
                s = arr[left][1]
                cnt[s] = cnt[s] - 1
                if cnt[s] == 0:
                    active = active - 1
                left = left + 1
            ans[idx] = n - active
        return ans