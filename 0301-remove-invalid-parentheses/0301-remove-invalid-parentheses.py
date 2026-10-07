class Solution:
    def removeInvalidParentheses(self, s):
        def check(s):
            count = 0
            for ch in s:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0
        level = {s}
        while True:
            ans = []
            for x in level:
                if check(x):
                    ans.append(x)
            if ans:
                return ans
            next_level = set()
            for x in level:
                for i in range(len(x)):
                    if x[i] == '(' or x[i] == ')':
                        next_level.add(x[:i] + x[i+1:])
            level = next_level