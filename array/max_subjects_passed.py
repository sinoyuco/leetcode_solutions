def maxSubjectsPassed(needed, answered, q):
    # if not answered:
    #     return 0
    differences = []
    for i in range(len(needed)):
        diff = needed[i] - answered[i]
        if diff > 0:
            differences.append(diff)
    ct = 0
    while differences and q >= differences[0]
        q -= differences.pop(0)
        ct+=1
    return ct
