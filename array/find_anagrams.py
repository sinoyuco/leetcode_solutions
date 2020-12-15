import collections
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cp = Counter(p)
        res = []
        for i in range(0, ls-lp+1):
            if Counter(s[i:i+lp]) == cp:
                res.append(i)
        return res
