class Solution:
    def maxDepth(self, s: str) -> int:
        cur=0
        ans=0
        for c in s:
            if c=='(':
                cur+=1
                ans=max(ans,cur)
            elif c==')':
                cur-=1
        return ans