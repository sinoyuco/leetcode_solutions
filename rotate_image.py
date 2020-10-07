class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        for j in range(len(matrix)):
            tba = []
            for i in range(len(matrix[0])-1, -1, -1):
                tba.append(matrix[i][j])
            matrix.append(tba)

            if j == l-1:
                for _ in range(l):
                    del matrix[0]
        return matrix
