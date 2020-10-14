class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count,sumt = 0,0
        maps = {}
        maps[0] = 1
        for i in range(len(nums)):
            sumt += nums[i]
            if sumt-k in maps:
                count+= maps[sumt-k]
            maps[sumt] = maps[sumt]+1 if sumt in maps else 1
            
        return count