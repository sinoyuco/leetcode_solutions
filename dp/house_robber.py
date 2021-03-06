class Solution:
    def rob(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0
        # if len(nums) < 3:
        #     return max(nums)
        # dp = [0]*len(nums)
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])
        # for i in range(2, len(nums)):
        #     dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        # return dp[-1]

        p1 = p2 = max_val = 0
        for i in range(len(nums)):
            max_val = max(p2+nums[i], p1)
            p2 = p1
            p1 = max_val
        return max_val
