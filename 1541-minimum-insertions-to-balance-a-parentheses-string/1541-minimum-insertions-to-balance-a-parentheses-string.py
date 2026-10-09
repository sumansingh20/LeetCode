class Solution:
    def minInsertions(self, s: str) -> int:
        ans = 0
        req = 0        
        for char in s:
            if char == '(':
                if req % 2 != 0:
                    ans += 1
                    req -= 1
                req += 2
            else:
                req -= 1
                if req < 0:
                    ans += 1
                    req += 2
        return ans + req