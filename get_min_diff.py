def getMinimumDifference(a, b):
    # Write your code here
    result = []
    i = 0
    while i < len(a):
        if len(a[i]) != len(b[i]):
            result.append(-1)
        else:
            map1 = {}
            for x in a[i]:
                if x in map1:
                    map1[x] += 1
                else:
                    map1[x] = 1
            for y in b[i]:
                if y in map1:
                    map1[y] -= 1
            result.append(sum([i for i in map1.values() if i > 0]))
        i += 1
    return result
