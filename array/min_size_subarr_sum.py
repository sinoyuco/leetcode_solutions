class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        res = math.inf
        l = sumval = 0
        for i in range(len(nums)):
            sumval += nums[i]
            while sumval >= s:
                res = min(res, (i+1)-l)
                sumval -= nums[l]
                l += 1

        return res if res != math.inf else 0
