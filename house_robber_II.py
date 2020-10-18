class Solution:
    def helper(self, nums, i, j):
        p1 = p2 = max_val = 0
        for idx in range(i, j):
            max_val = max(p2+nums[idx], p1)
            p2 = p1
            p1 = max_val
        return max_val

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums, 1, len(nums)), self.helper(nums, 0, len(nums)-1))
