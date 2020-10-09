def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
    maps = {}
    end = max(i[2] for i in trips)
    start = min(i[1] for i in trips)

    for i in trips:
        if i[1] in maps:
            maps[i[1]] += i[0]
        else:
            maps[i[1]] = i[0]

        if i[2] in maps:
            maps[i[2]] -= i[0]
        else:
            maps[i[2]] = -i[0]

    count = 0
    
    for i in range(start, end+1):
        if i in maps: zxgn bv
            count += maps[i]
        if count > capacity:
            return False

    return True
