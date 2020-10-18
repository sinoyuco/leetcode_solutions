def abdifference(arr):
    arr = sorted(arr)

    return [arr[0], arr[-1]]


print(abdifference([-1,-10,8,2,0,5,3]))
