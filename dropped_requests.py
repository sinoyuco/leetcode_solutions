def droppedRequests(requestTime):
    # Write your code here
    fails = 0
    maps = {}
    for i in range(len(requestTime)):

        k = requestTime[i]

        #3 a second
        if k not in maps:
            maps[k] = 1
        else:
            maps[k] += 1
            if maps[k] >= 4:
                fails += 1

        print(maps[k])

        #20 in 10 seconds
        if i >= 20:
            sub = requestTime[(i-20):i+1]
            print(i)
            print(sub)
            if (sub[-1] - sub[0]) < 10:
                fails += 1

        #60 in a minute
        if i >= 60:
            sub = requestTime[(i-60):i+1]
            if (sub[-1] - sub[0]) < 60:
                fails += 1
    return fails
