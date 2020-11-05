class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # nums = [-1,3,2,0]
        # m = [0, 0, 0, 0]
        minUntil = [0]*len(nums)
        minUntil[0] = nums[0]
        for i in range(1, len(nums)):
            minUntil[i] = min(minUntil[i-1], nums[i])

        stack = []
        for j in range(len(nums)-1, 0, -1):
            while stack and nums[stack[-1]] < nums[j]:
                if nums[stack[-1]] > minUntil[j-1]:
                    return True
                stack.pop()
            stack.append(j)
        return False
