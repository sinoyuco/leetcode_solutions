def areAlmostEquivalent(s, t):
    # Write your code here
    result = []
    for j in range(len(s)):
        # if len(s[j]) is not len(t[j]):
        #     print('not equal')
        #     result.append('NO')
        #     continue

        maps = {}
        for i in range(len(s[j])):
            if s[j][i] not in maps:
                maps[s[j][i]] = 1
            else:
                maps[s[j][i]] += 1

            if t[j][i] not in maps:
                maps[t[j][i]] = -1
            else:
                maps[t[j][i]] -= 1

        if max(maps.values()) > 3 or min(maps.values()) < -3:
            result.append('NO')
        else:
            result.append('YES')

    return result
