class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2:
            return False
        target = s // 2
        seen = set()
        seen.add(0)
        for val in nums:
            current = set()
            for pre in seen:
                current.add(pre)
                if pre + val == target:
                    return True
                current.add(pre + val)
            seen = current
        return False
