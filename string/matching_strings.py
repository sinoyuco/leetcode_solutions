def matchingStrings(strings, queries):
    maps = {}
    for i in strings:
        if i in maps:
            maps[i] += 1
        else:
            maps[i] = 1

    return [maps[i] if i in maps else 0 for i in queries]
