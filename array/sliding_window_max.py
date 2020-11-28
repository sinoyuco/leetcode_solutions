class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        if len(nums) <= k:
            return [max(nums)]

        stack = []
        result = []
        for i in range(len(nums)):
            if stack and i-k >= stack[0][1]:
                stack.pop(0)
            while stack and nums[i] > stack[-1][0]:
                stack.pop()
            stack.append((nums[i], i))
            if i >= k - 1:
                result.append(stack[0][0])
        return result
