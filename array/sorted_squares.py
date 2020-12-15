import math


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        m = mo = math.inf
        for i in range(len(nums)):
            if abs(nums[i]) < m:
                m = abs(nums[i])
                mo = i
        res = [nums[mo]**2]

        l, r = mo-1, mo+1

        while len(res) != len(nums):
            if l < 0:
                res.append(nums[r]**2)
                r += 1
            elif r >= len(nums):
                res.append(nums[l]**2)
                l -= 1
            else:
                if abs(nums[l]) < abs(nums[r]):
                    res.append(nums[l]**2)
                    l -= 1
                else:
                    res.append(nums[r]**2)
                    r += 1
        return res
