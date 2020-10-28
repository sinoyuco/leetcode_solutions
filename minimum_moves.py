def minimumMoves(arr1, arr2):
    # Write your code here
    ct = 0
    for i in range(len(arr1)):
        a, b = str(arr1[i]), str(arr2[i])
        for j in range(len(a)):
            ct += abs(int(a[j]) - int(b[j]))
    return ct
