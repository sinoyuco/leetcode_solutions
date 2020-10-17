import collections
def characters_with_highest_frequency(word):
    # ct = collections.Counter(word)
    # sortedct = sorted(ct.items(), key=lambda x:[1], reverse=True)
    # return [k for k,v in sortedct if v==sortedct[0][1]]

    ct = collections.Counter(word)

    maxv,result = 0, []
    for k,v in ct.items():
        print(maxv, k ,v)
        if v == maxv:
            result.append(k)
        elif v > maxv:
            maxv = v
            result = [k]
    return result

print(characters_with_highest_frequency('ananin ami'))
