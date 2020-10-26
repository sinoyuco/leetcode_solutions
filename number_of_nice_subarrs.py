from collections import defaultdict
def numberOfNiceSubarrays(nums, k):
    if not nums:
        return 0
    maps = defaultdict(int)
    maps[0] = 1
    curr = result = 0
    for i in range(len(nums)):
        if nums[i]%2==1:
            curr+=1
        if curr-k in maps:
            result+=maps[curr-k]
        maps[curr]+=1
    return result