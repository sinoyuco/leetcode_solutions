def one_away(str1,str2):
    maps = {}
    for i in range(len(str1)):
        if str1[i] in maps:
            maps[str1[i]] += 1
        else:
            maps[str1[i]] = 1

    for i in range(len(str2)):
        if str2[i] in maps:
            maps[str2[i]] -= 1
        else:
            maps[str2[i]] = -1

    p = []
    for k,v in maps.items():
        if v!=0:
            if len(p)==2:
                return False
            elif len(p) == 1:
                if v is not -p[0]:
                    return False
                else:
                    p.append(v)
            else:
                p.append(v)
    return True

print(one_away('pale', 'ple'))
print(one_away('palea', 'pale'))
print(one_away('pale', 'kale'))
print(one_away('pale', 'bake'))

