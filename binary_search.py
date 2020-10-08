class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        mid = len(nums)//2

        if nums[mid] == target:
            print(nums, mid)
            return mid
        elif target < nums[mid]:
            return self.search(nums[:mid], target)
        else:
            a = self.search(nums[mid+1:], target)
            print(nums, mid)
            return a + (mid+1) if a is not -1 else -1
