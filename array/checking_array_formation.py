import collections
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        maps = collections.defaultdict(list)
        for i in pieces:
            maps[i[0]] = i
        
        idx = 0
        while idx < len(arr):
            if arr[idx] in maps:
                temp = maps[arr[idx]]
                for t in range(len(temp)):
                    if temp[t] != arr[idx]:
                        return False
                    idx+=1
            else:
                return False
        return True