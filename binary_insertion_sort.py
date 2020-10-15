class Solution:
    def bs(self, array, target, low, high):
        if low == high:
            return low if array[low]>target else low+1
        
        if low > high:
            return low

        mid = (low+high)//2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            return self.bs(array,target,mid+1,high)
        else:
            return self.bs(array, target, low, mid-1)

    def insertion_sort(nums):
        for i in range(1,len(nums)):
            curr = nums[i]
            bscall = self.bs(nums, curr, 0, i-1)
            nums = nums[:bscall] + [curr] + nums[bscall:i] + nums[i+1:]
        return nums

a = Solution()
print(a.bs([1,2,4,6,8],9, 0, 5))
