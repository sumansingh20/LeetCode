class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        mod=1000000007
        N=n+k-1
        r=2*k
        ans=1
        for i in range(1,r+1):
            ans=ans*(N-r+i)%mod
            ans=ans*pow(i,mod-2,mod)%mod
        return ans