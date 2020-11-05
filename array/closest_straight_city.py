import math


def closestStraightCity(c, x, y, q):
    # Write your code here
    result = []
    for i in range(len(q)):
        mind = math.inf
        cname = ''
        for j in range(len(c)):
            if q[i] != c[j] and (x[i] == x[j] or y[i] == y[j]):
                if abs(x[i]-x[j])+abs(y[i]-y[j]) == mind:
                    if len(c[j]) < len(cname):
                        cname = c[j]
                elif abs(x[i]-x[j])+abs(y[i]-y[j]) < mind:
                    mind = abs(x[i]-x[j])+abs(y[i]-y[j])
                    cname = c[j]
        if cname == '':
            result.append('NONE')
        else:
            result.append(cname)
    return result
