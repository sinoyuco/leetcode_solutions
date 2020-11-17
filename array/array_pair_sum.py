class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # loglinear
        nums.sort()
        i = m = 0
        while i < len(nums):
            m += nums[i]
            i += 2
        return m
