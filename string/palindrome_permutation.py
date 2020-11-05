import collections
def palindrome_perm(str):
    maps = collections.Counter(str)

    bol = False
    for k,v in maps.items():
        if v%2==1:
            if bol:
                return False
            bol = True
    return True

print(palindrome_perm('tacacott'))
print(palindrome_perm('tacacot'))

