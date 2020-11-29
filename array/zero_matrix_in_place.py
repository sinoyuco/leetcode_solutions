class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        h,w = len(matrix), len(matrix[0])
        r,c = set(), set()
        for i in range(h):
            for j in range(w):
                if matrix[i][j] == 0:
                    r.add(i)
                    c.add(j)
                    
        for i in range(h):
            for j in range(w):
                if i in r or j in c:
                    matrix[i][j] = 0