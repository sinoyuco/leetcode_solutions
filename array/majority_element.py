import collections
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maps = collections.defaultdict(int)
        for i in nums:
            maps[i] += 1
            if maps[i] > len(nums)/2:
                return i
