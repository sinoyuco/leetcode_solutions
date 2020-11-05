def numSubarrayProductLessThanK(nums, k):
    output = 0
    start = -1
    product = 1
    for i in range(len(nums)):
        if nums[i] < k:
            product *= nums[i]
            while product >= k:
                start += 1
                product //= nums[start]
                print(f'prod is {product}')
            output += i-start
            print(nums[i], output)
        else:
            start = i
    return output
    
    
print(numSubarrayProductLessThanK([10,5,2,6],100))
