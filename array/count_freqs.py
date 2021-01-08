def countSignals(frequencies, filterRanges):
    # Write your code here
    res = 0
    for s in frequencies:
        n = True
        for i in range(len(filterRanges)):
            filt = filterRanges[i]
            if s < filt[0] or s > filt[1]:
                n = False
                break
        if n:
            res += 1
    return res
