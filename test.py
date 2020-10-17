def substituteElementsGreater(arr,k):

    #[40, 20, 10, 30], 70  -> 20

    #[10,20,30,40] -> [30,40], k=70-30 = 40
    arr = sorted(arr)
    for i in range(len(arr)):
        rest = arr[i:]
        if k/len(rest) <= arr[i]:
            return k/len(rest)
        k-=arr[i]
