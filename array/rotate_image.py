def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    l = len(matrix)
    for j in range(l):
        tba = []
        for i in range(len(matrix[0])-1, -1, -1):
            tba.append(matrix[i][j])
        matrix.append(tba)

        if j == l-1:
            for _ in range(l):
                del matrix[0]
    return matrix

matrix = [[1,2],[3,4]]
print(rotate(matrix))
