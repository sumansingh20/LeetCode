class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def merge(a, b):
            ans = set()
            for x in a:
                for y in b:
                    ans.add(x + y)
            return ans
        def parse(i):
            cur = {""}
            total = set()
            while i < len(expression) and expression[i] != '}':
                if expression[i] == ',':
                    total |= cur
                    cur = {""}
                    i += 1
                elif expression[i] == '{':
                    s, i = parse(i + 1)
                    cur = merge(cur, s)
                else:
                    cur = merge(cur, {expression[i]})
                    i += 1
            total |= cur
            if i < len(expression) and expression[i] == '}':
                i += 1
            return total, i
        ans, _ = parse(0)
        return sorted(ans)