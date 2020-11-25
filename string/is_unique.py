def is_unique(s):
    
    # O(n) time and space
    maps = {}
    for i in range(len(s)):
        if s[i] in maps:
            return False
        maps[s[i]] = 1
    return True

    #can this be solved with no additional space, linearly?
    