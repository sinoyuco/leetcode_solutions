class Solution:
    def sortColors(self, nums: List[int]) -> None:
        if len(nums) < 2:
            return nums

        i = j = 0
        while j < len(nums):
            if nums[i] == 2:
                del nums[i]
                nums.append(2)
                i -= 1
            elif nums[i] == 0:
                del nums[i]
                nums.insert(0, 0)
            i += 1
            j += 1
        return nums
