class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        def bs(arr, start, end, tar):
            if start > end:
                return start
            mid = (start+end)//2
            if arr[mid] == tar:
                return mid
            elif nums[mid] > tar:
                return bs(arr, start, mid-1, tar)
            else:
                return bs(arr, mid+1, end, tar)

        return bs(nums, 0, len(nums)-1, target)
