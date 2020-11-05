import collections
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        l = set(arr2)
        y, n = [], []
        maps = {}
        for i in arr1:
            if i in l:
                if i in maps:
                    maps[i] += 1
                else:
                    maps[i] = 1
            else:
                n.append(i)

        for j in arr2:
            y += [j]*(maps[j])
        return y+sorted(n)
