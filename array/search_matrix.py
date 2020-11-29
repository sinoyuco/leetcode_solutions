class Solution: 
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        h,w = len(matrix), len(matrix[0])
        resi,resj = 0, w-1
        while resi < h and resj >= 0:
            if matrix[resi][resj] == target: return True
            elif target > matrix[resi][resj]:
                resi+=1
            else:
                resj -=1
        return False