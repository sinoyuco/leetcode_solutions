class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i, j = 0, len(arr)-1
        while i < len(arr)-1 and arr[i] < arr[i+1]:
            i += 1
        while j > 0 and arr[j-1] > arr[j]:
            j -= 1
        return i == j and i > 0 and j < len(arr)-1


        # switched = False
        # up = False
        # for i in range(1, len(arr)):
        #     if arr[i] == arr[i-1]:
        #         return False
            
        #     if arr[i] > arr[i-1]:
        #         up = True
            
        #     if switched:
        #         if arr[i] >= arr[i-1]:
        #             return False
        #     else:
        #         if arr[i] <= arr[i-1]:
        #             switched = True
                    
        # return True if up and switched else False
