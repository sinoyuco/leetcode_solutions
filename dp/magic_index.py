class Solution:
    def magic_index(self, arr):    
        return self.bs(arr, 0, len(arr)-1)

    def bs(self, arr, start, end):
        if end < start:
            return -1
        mid = (start+end)//2
        if arr[mid] == mid:
            return mid:
        elif mid < arr[mid]:
            return self.bs(arr, mid+1, end)
        else:
            return self.bs(arr, start, mid-1)