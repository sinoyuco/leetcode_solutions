class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for i in range(n)] for j in range(n)]
        seen = set()
        i,j = 0,-1
        curr = 1
        div = 0
        dir = [(0,1), (1,0), (0, -1), (-1,0)]
        while curr <= n**2:
            curri, currj = i+dir[div%4][0], j+dir[div%4][1]
            if 0 <= curri < n and 0 <= currj < n and matrix[curri][currj] == 0:
                matrix[curri][currj] = curr
                i+=dir[div%4][0]
                j+=dir[div%4][1]
                curr+=1
            else:
                div+=1
        return matrix