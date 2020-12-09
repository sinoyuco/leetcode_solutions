import collections
class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        arr = [0]
        for i in A:
            arr.append(arr[-1]+i)
        c,res = collections.Counter(),0
        for i in arr:
            res+=c[i]
            c[i+S] += 1
        return res