class Solution:
    def reverseParentheses(self, s: str) -> str:
        a=[]
        for c in s:
            if c==')':
                b=[]
                while a[-1]!='(':
                    b.append(a.pop())
                a.pop()
                a+=b
            else:
                a.append(c)
        return ''.join(a)