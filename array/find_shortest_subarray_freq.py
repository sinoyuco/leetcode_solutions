class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        maps = {}
        for i in range(len(nums)):
            if nums[i] in maps:
                maps[nums[i]].append(i)
            else:
                maps[nums[i]] = [i]
        freq = max(map(len, maps.values()))

        minval = math.inf
        for k, v in maps.items():
            print(k, v)
            if len(v) == freq:
                minval = min(minval, v[-1]-v[0]+1)
        return minval
