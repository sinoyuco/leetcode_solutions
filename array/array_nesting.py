class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        maxval = 0
        seen = set()
        for i in range(len(nums)):
            if i not in seen:
                j = i
                c = 0
                while j not in seen:
                    seen.add(j)
                    j = nums[j]
                    c+=1
                maxval = max(c, maxval)
        return maxval