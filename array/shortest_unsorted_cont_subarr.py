class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:

        #loglinear
        # a = sorted(nums)
        # mi, ma = len(nums), 0
        # for i in range(len(a)):
        #     if a[i] != nums[i]:
        #         mi = min(mi, i)
        #         ma = max(ma, i)
        # return ma-mi+1 if ma-mi >= 0 else 0


        #linear
        l, r = 0, len(nums) - 1
        while l < len(nums)-1 and nums[l] <= nums[l+1]:
            l += 1
        if l == len(nums)-1:
            return 0
        while r > 0 and nums[r] >= nums[r-1]:
            r -= 1
        sub = nums[l:(r+1)]
        mi, ma = min(sub), max(sub)

        while l > 0 and nums[l-1] > mi:
            l -= 1
        while r < len(nums)-1 and nums[r+1] < ma:
            r += 1
        return (r-l)+1
