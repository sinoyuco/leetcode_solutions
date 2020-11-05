def countPairs(numbers, k):
    # Write your code here
    a = set()
    for i in range(len(numbers)):
        cu = numbers[i]-k
        if cu in a:
            continue
        else:
            a.add(cu)
    
    count = 0
    for i in range(len(numbers)):
        if numbers[i] in a:
            count+=1
            a.remove(numbers[i])
    return count
