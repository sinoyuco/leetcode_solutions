import math


def efficientJanitor(weight):
    # Write your code here
    tot = ct = 0
    for i in range(len(weight)):
        tot += weight[i]
        if tot > 3:
            ct += 1
            tot -= 3
    return ct
