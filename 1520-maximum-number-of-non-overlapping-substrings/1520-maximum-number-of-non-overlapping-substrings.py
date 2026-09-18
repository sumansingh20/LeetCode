class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first=[len(s)]*26
        last=[-1]*26
        for i,c in enumerate(s):
            x=ord(c)-97
            first[x]=min(first[x],i)
            last[x]=i
        a=[]
        for x in range(26):
            if last[x]==-1:
                continue
            l=first[x]
            r=last[x]
            i=l
            ok=True
            while i<=r:
                y=ord(s[i])-97
                if first[y]<l:
                    ok=False
                    break
                r=max(r,last[y])
                i+=1
            if ok:
                a.append((l,r))
        a.sort(key=lambda x:x[1])
        ans=[]
        end=-1
        for l,r in a:
            if l>end:
                ans.append(s[l:r+1])
                end=r
        return ans