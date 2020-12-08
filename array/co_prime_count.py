import math
def coprimeCount(A):
    # Write your code h
    res = []
    for num in A:
        count = 0
        for i in range(1, num//2+1):
            if i == 1 or math.gcd(i, num) == 1:
                count+=2
        res.append(count)
    return res



print(coprimeCount([5,8,14]))
# [4,4,6]
# [1,2,3,4], []
