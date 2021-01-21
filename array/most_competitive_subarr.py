class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        l = len(nums)
        res = []
        p = l-k
        res.append(nums[0])
        i = 1
        while i < l:
            if p == 0:
                return res + nums[i:]
            elif res and nums[i] < res[-1]:
                res.pop()
                p -= 1
            else:
                res.append(nums[i])
                i += 1
        return res[:k]
