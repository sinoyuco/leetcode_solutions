class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        ma = mi = res = nums[0]
        for j in range(1,len(nums)):
            i = nums[j]
            ma,mi = max(i*ma, i*mi, i), min(i*mi, i*ma, i)
            res = max(res, ma)
        return res