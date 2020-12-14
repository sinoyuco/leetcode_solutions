class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        memo = {}
        
        def dfs(arr, s, c):
            if (s,c) in memo:
                return memo[(s,c)]
            if c == len(arr):
                if s == 0:
                    return 1
                else:
                    return 0
            decrement = dfs(nums, s-nums[c], c+1)
            increment = dfs(nums, s+nums[c], c+1)
            res = decrement + increment
            memo[(s,c)] = res
            return res
        
        return dfs(nums, S, 0)