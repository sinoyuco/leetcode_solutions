import math


def finalInstances(instances, averageUtil):
    # Write your code here
    i = 0
    while i < len(averageUtil):
        j = averageUtil[i]
        if 25 <= j <= 60:
            i += 1
        elif j < 25:
            if instances != 1:
                instances = math.ceil(instances / 2)
                i += 10
            else:
                i += 1
        else:
            if instances * 2 < (2 * 10**8):
                instances = instances*2
                i += 10
            else:
                i += 1

    return instances
