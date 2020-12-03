class Solution:
    def bs(self, arr, start, end):
        if start == end:
            return start
        mid = (start+end)//2
        if arr[mid] > arr[mid+1]:
            return self.bs(arr,start,mid)
        else:
            return self.bs(arr, mid+1, end)
        
        
    def findPeakElement(self, nums: List[int]) -> int:
        return self.bs(nums, 0 , len(nums)-1)