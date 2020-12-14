def divisibleSumPairs(n, k, ar):
    bucket = [0]*k
    count = 0
    for i in ar:
        modv = i % k
        count += bucket[(k-modv)%k]
        bucket[modv] += 1
    return count


print(divisibleSumPairs(6, 3,[1,3,2,6,1,2]))