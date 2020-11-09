def getSubsets(s):
    if len(s)==1:
        print(s)
        return [s,[]]
    
    result = []
    for i in getSubsets(s[1:]):
        result.append([s[0]]+i)
        result.append(i)
    return result


print(getSubsets([1,2,3]))
