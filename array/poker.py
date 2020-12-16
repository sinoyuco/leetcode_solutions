import collections
def poker(p1,p2):
    maps1 = collections.Counter(p1)
    maps2 = collections.Counter(p2)
    stack1, stack2 = [], []
    for k,v in maps1.items():
        stack1.append((k,v))
    for k, v in maps2.items():
        stack2.append((k, v))

    while stack1 and stack2:
        k1,v1 = stack1[-1]
        k2,v2 = stack2[-1]
        if v2 > v1:
            return 'p2'
        elif v1 > v2:
            return 'p1'
        else:
            if k1 < k2:
                return 'p2'
            elif k2 < k1:
                return 'p1'
            else:
                stack1.pop()
                stack2.pop()

    return 'tie'
    
    # [7: 2, 8:-2]
