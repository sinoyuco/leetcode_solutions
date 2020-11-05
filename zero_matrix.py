def zero_matrix(matrix):
    m = [r[:] for r in matrix]
    if not matrix:
        return matrix
    h,w = len(matrix), len(matrix[0])
    
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 0:
                
                for x in range(h):
                    m[x][j] = 0
                for y in range(w):
                    m[i][y] = 0
    return m


matrix = [[1,2,3], [4,5,6], [7,8,9]]
matrix1 = [[1,2,3], [4,0,6], [7,8,9]]
matrix2 = [[0, 2, 3], [4, 5, 6], [7, 8, 0]]

print(zero_matrix(matrix))
print(zero_matrix(matrix1))
print(zero_matrix(matrix2))
