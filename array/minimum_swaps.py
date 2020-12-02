def minimumSwaps(popularity):
    # Write your code here
    [4,1,2,3]
    ct = 0
    seen = set()
    s = len(popularity)
    for i in range(s):
        if i+popularity[i] == s:
            continue
        else:
            pretender = popularity[s-popularity[i]]
            if popularity[i] in seen:
                continue
            elif pretender + i == s:
                ct+=1
                seen.add(pretender)
    return ct