class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        l = len(nums)
        res = []
        c, p = 0, l-k
        res.append(nums[0])
        i = 1
        while i < l:
            if p == 0:
                return res + nums[i:]
            elif res and nums[i] < res[-1]:
                res.pop()
                c -= 1
                p -= 1
            else:
                res.append(nums[i])
                c += 1
                i += 1
        return res[:k]
