def unsortedTwoToSorted(arr1,arr2):
    # newarr = arr1+arr2
    # return sorted(newarr)
    res
    a,b = sorted(a), sorted(b)

    i = j = k = 0
    result = ['' for i in range(len(a)+len(b))]
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            res[k] = a[i]
            i+=1
        else:
            res[k] = b[j]
            j+=1
        k+=1
    
    while i < len(a):
        res[k] = a[i]
        i+=1
        k+=1
    while j < len(b):
        res[k] = b[j]
        j += 1
        k += 1
    return result

