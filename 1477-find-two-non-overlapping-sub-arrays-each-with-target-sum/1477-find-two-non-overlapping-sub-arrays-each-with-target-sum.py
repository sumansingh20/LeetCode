class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n=len(arr)
        dp=[1000000]*n
        left=0
        total=0
        best=1000000
        ans=1000000
        for right in range(n):
            total+=arr[right]
            while total>target:
                total-=arr[left]
                left+=1
            if total==target:
                length=right-left+1
                if left>0:
                    ans=min(ans,length+dp[left-1])
                best=min(best,length)
            dp[right]=best
        if ans==1000000:
            return -1
        return ans