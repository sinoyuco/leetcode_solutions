def array_addition(arr):
    arr.sort()
    target = arr.pop()

    def dfs(tar, nums):
        if len(nums)==0:
            return tar==0

        num_to_check = nums[0]
        nums = nums[1:]
        
        return dfs(tar, nums) or dfs(tar-num_to_check, nums)

    return dfs(target, arr)

print(array_addition([1,8,6,2]))

