def getSequenceSum(i, j, k):
    s = 0
    if i > k:
        for x in range(k, i):
            s += x
        for y in range(i, j+1):
            s += 2*y
    else:
        for x in range(i, k):
            s += x
        for y in range(k, j+1):
            s += 2*y
    return s-j


