def countPairs(numbers, k):
    # Write your code here
    count = 0
    maps = {}
    for i in range(len(numbers)):
        if numbers[i] not in maps:
            maps[numbers[i]] = True

        if numbers[i]-k in maps and maps[numbers[i]-k]:
            maps[numbers[i]-k] = False
            count += 1
        if numbers[i]+k in maps and maps[numbers[i]+k]:
            maps[numbers[i]+k] = False
            count += 1

    return count
