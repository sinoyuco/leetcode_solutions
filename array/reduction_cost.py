def reductionCost(nums):
    # Write your code here
    # how to do it linear / loglinear?
    tot = 0
    while len(nums) > 1:
        m_idx = nums.index(min(nums))
        m1 = nums.pop(m_idx)

        m_idx = nums.index(min(nums))
        m2 = nums.pop(m_idx)

        tot += (m1+m2)
        nums.append(m1+m2)
    return tot

    




print(reductionCost([4,4,4,4,6]))

print(reductionCost([4,8,6]))

print(reductionCost([1,2,3]))
    
