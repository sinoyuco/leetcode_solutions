def quicksort(nums):
    if not nums:
        return nums
    left,right = [], []
    pivot = nums.pop()
    for i in range(len(nums)):
        if nums[i] < pivot:
            left.append(nums[i])
        else:
            right.append(nums[i])
    
    return quicksort(left) + [pivot] + quicksort(right)


print(quicksort([1,4,3,6,7,11,-2]))