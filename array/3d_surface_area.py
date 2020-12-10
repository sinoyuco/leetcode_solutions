def surfaceArea(A):
    h, w = len(A), len(A[0])
    res = 0
    for i in range(h):
        for j in range(w):
            curr = A[i][j]
            area = 2+(curr*4)
            if i > 0:
                area -= min(curr, A[i-1][j]) * 2
            if j > 0:
                area -= min(curr, A[i][j-1]) * 2
            res += area

    return res
