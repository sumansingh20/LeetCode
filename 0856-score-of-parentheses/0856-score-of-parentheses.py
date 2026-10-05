class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[0]
        for x in s:
            if x=='(':
                stack.append(0)
            else:
                v=stack.pop()
                if v==0:
                    v=1
                else:
                    v*=2
                stack[-1]+=v
        return stack[0]