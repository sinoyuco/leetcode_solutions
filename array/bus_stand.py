def kthPerson(k, p, q):
    # Write your code here
    res = []
    for i in range(len(q)):
        bus_arrival = q[i]
        n = last = 0
        for j in range(len(p)):
            if n == k:
                break
            if p[j] >= bus_arrival:
                n += 1
                last = j+1
        if n == k:
            res.append(last)
        else:
            res.append(0)
    return res
