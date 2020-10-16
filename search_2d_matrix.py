class Solution:
    def bs(self, arr, target):
        if len(arr) == 0:
            return -1

        mid = len(arr)//2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return self.bs(arr[:mid], target)
        else:
            rhs = self.bs(arr[mid+1:], target)
            return -1 if rhs == -1 else rhs + (mid+1)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        for i in matrix:
            if target == i[-1]:
                return True
            elif target < i[-1]:
                return False if self.bs(i[:-1], target) == -1 else True
        return False
