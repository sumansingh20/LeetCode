class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        a=[]
        for i in range(len(intervals)):
            a.append([intervals[i][0],intervals[i][1],intervals[i][2],i])
        a.sort()
        n=len(a)
        starts=[x[0] for x in a]
        dp=[[0]*5 for _ in range(n+1)]
        ans=[[[] for _ in range(5)] for _ in range(n+1)]

        for i in range(n-1,-1,-1):
            for k in range(1,5):
                l=i+1
                r=n
                while l<r:
                    mid=(l+r)//2
                    if starts[mid]>a[i][1]:
                        r=mid
                    else:
                        l=mid+1
                j=l

                x=a[i][2]+dp[j][k-1]
                y=dp[i+1][k]
                ids=sorted([a[i][3]]+ans[j][k-1])

                if x>y or x==y and ids<ans[i+1][k]:
                    dp[i][k]=x
                    ans[i][k]=ids
                else:
                    dp[i][k]=y
                    ans[i][k]=ans[i+1][k]

        return ans[0][4]