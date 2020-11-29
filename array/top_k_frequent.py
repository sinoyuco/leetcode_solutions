from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        b = [[] for i in range(len(nums)+1)]
        a = Counter(nums)
        for key,val in a.items():
            b[val].append(key)
        res = [i for j in b for i in j]
        return res[::-1][:k]