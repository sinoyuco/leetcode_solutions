import collections
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        c = collections.Counter(nums)
        # maps = {}
        count = 0
        # for i in range(len(nums)):
        #     curr = nums[i]
        #     if k-curr in maps:
        #         if k-curr == curr:
        #             if c[curr]>1:
        #                 count+=1
        #                 c[curr] -=1
        #                 c[k-curr] -= 1
        #         else:
        #             if c[curr]>0 and c[k-curr]>0:
        #                 count+=1
        #                 c[curr] -=1
        #                 c[k-curr] -= 1
        #     maps[curr] = i
        # return count
        for i in c:
            if i * 2 == k:
                count += math.floor(c[i]/2)
            elif i <= k/2 and k-i in c:
                count += min(c[i], c[k-i])
        return count
