def playSegments(coins):
    # Write your code here
    for i in range(len(coins)):
        p1 = p2 = 0
        p1s, p2s = coins[:i], coins[i:]
        for j in p1s:
            if j != 0:
                p1 += j
            else:
                p1 -= 1
        if p1 > len(p2s):
            return i
        for k in p2s:
            if k != 0:
                p2 += k
            else:
                p2 -= 1
        if p1 > p2:
            return i
