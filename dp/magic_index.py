class Solution:
    #elements in array are distinct, sorted integers.
    def magic_index(self, arr):    
        return self.bs(arr, 0, len(arr)-1)

    def bs(self, arr, start, end):
        if end < start:
            return -1
        mid = (start+end)//2
        if arr[mid] == mid:
            return mid:
        elif mid < arr[mid]:
            #look at right subarray
            return self.bs(arr, start, mid-1)
        else:
            #look at left subarray
            return self.bs(arr, mid+1, end) 
