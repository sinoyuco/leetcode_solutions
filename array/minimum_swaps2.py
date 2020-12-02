def minimumSwaps2(arr):
    ct = i = 0
    while i < len(arr):
        if arr[i] == i+1:
            i += 1
        else:
            truepos = arr[i]-1
            arr[i], arr[truepos] = arr[truepos], arr[i]
            ct += 1
    return ct
