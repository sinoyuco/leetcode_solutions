def findTheDifference(self, s: str, t: str) -> str:
    maps = {}
    for i in s:
        if i in maps:
            maps[i] -= 1
        else:
            maps[i] = -1

    for j in t:
        if j in maps:
            if maps[j] == 0:
                return j
            maps[j] += 1
        else:
            return j
