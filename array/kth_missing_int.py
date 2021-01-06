class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        curr,n = 0, len(arr)+k
        for i in range(1,n+1):
            if curr >= len(arr) or arr[curr] != i:
                k-=1
            else:
                curr+=1
            if k==0:
                return i