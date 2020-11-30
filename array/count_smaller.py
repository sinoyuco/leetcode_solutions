from bisect import bisect_left
from collections import deque
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        result = deque([0])
        num_r = [nums[-1]]

        for i in range(len(nums)-2, -1, -1):
            idx = bisect_left(num_r, nums[i])
            num_r.insert(idx, nums[i])
            result.appendleft(idx)

        return result
