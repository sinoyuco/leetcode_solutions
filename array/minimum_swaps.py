def minimumSwaps(popularity):
    # Write your code here
    i = ct = 0
    s = len(popularity)
    while i < len(popularity):
        if i + popularity[i] == s:
            i+=1
        else:
            truepos = s-i
            popularity[s], popularity[truepos] = popularity[truepos], popularity[s]
            ct+=1
            i-=1
    return ct

