import collections
def isAnagram(s,t):
    cnt = collections.Counter(s)
    
    for i in t:
        if i in cnt:
            cnt[i] -= 1
        else:
            return False
    
    
    for j in cnt.values():
        if j is not 0: 
            return False
    return True
    

print(isAnagram('aacc','ccac'))


