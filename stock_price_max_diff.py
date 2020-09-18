def maxDifference(px):
    # BRUTE FORCE
    if len(px) < 2:
        return -1

    maxdiff = 0
    for i in range(len(px)):
        a = max(px[i:])
        if (a - px[i]) > maxdiff:
            maxdiff = (a-px[i])

    return -1 if maxdiff == 0 else maxdiff
