class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        seen = set()
        t = str(sum([int(i)**2 for i in str(n)]))
        print(t)
        while t!='1':
            l = str(sum([int(i)**2 for i in t]))
            if l == '1': return True
            if l in seen:
                return False
            else:
                seen.add(l)
            t = l
        return True