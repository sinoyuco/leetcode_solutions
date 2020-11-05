import math


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_val,s = -math.inf, 0
        for i in nums:
            s+=i
            max_val = max(max_val, s)
            s = max(s,0)
        return max_val
