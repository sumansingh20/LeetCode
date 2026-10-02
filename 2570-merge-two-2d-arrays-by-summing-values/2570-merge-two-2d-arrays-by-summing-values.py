class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        a={}
        for x,y in nums1:
            a[x]=y
        for x,y in nums2:
            a[x]=a.get(x,0)+y
        ans=[]
        for x in sorted(a):
            ans.append([x,a[x]])
        return ans