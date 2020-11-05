def substituteElementsGreater(arr,k):

    #[40, 20, 10, 30], 70  -> 20

    #[10,20,30,40] -> [30,40], k=70-30 = 40

    # this is O(nlogn) because of the sort, is there a linear solution?
    arr = sorted(arr)
    for i in range(len(arr)):
        rest = len(arr)-i
        if k/rest <= arr[i]:
            return k/rest
        k-=arr[i]



