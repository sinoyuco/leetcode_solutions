class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        switched = False
        up = False
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                return False
            
            if arr[i] > arr[i-1]:
                up = True
            
            if switched:
                if arr[i] >= arr[i-1]:
                    return False
            else:
                if arr[i] <= arr[i-1]:
                    switched = True
                    
        return True if up and switched else False