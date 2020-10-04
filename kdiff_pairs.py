import collections


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        cntr = collections.Counter(nums)
        if k == 0:
            return len([k for k, v in cntr.items() if v > 1])
        uniq = set(nums)
        return len([i for i in uniq if i-k in uniq])
