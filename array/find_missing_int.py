def firstMissingPositive(self, nums: List[int]) -> int:

    # its linear (O(2n) == O(n)) as the problems asks, but a solution using sorting is against the purpose.

    nums = sorted(nums)
    smallest = 1
    for i in nums:
        if i > 0 and smallest >= i:
            smallest = i+1
    return smallest
