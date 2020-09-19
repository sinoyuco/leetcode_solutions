def maxDifference(px):
    # BRUTE FORCE
    # if len(px) < 2:
    #     return -1

    # maxdiff = 0
    # for i in range(len(px)):
    #     a = max(px[i:])
    #     if (a - px[i]) > maxdiff:
    #         maxdiff = (a-px[i])

    # return -1 if maxdiff == 0 else maxdiff

    mark = max(px)
    p = -1
    for i in range(len(px)):
        if px[i] < mark:
            mark = px[i]
        elif px[i] - mark > p:
            p = px[i] - mark
    return -1 if p == 0 else p

stockp = [7,1,3,5,2]
stocks = [6,2,1]
print(maxDifference(stockp)) # 4
print(maxDifference(stocks)) # -1
