def minMoves(arr):
    # Write your code here
    # [1,1,1,1,0,1,0,1]
    oc = dl = zc = dr = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            oc += 1
            dr += zc
        else:
            zc += 1
            dl += oc
    return min(dr, dl)
