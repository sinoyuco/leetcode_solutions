class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        a = sorted(nums)
        mi, ma = len(nums), 0
        for i in range(len(a)):
            if a[i] != nums[i]:
                mi = min(mi, i)
                ma = max(ma, i)
        return ma-mi+1 if ma-mi >= 0 else 0
