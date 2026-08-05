class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        data = [[] for i in range(n)]
        for arr in invocations:
            x = arr[0]
            y = arr[1]
            data[x].append(y)
        visited = [False] * n
        stack = [k]
        visited[k] = True
        while stack:
            x = stack.pop()
            for y in data[x]:
                if visited[y] == False:
                    visited[y] = True
                    stack.append(y)
        for arr in invocations:
            x = arr[0]
            y = arr[1]
            if visited[x] == False and visited[y] == True:
                ans = []
                for i in range(n):
                    ans.append(i)
                return ans
        ans = []
        for i in range(n):
            if visited[i] == False:
                ans.append(i)
        return ans