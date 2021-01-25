class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        lastEncounter = -1
        for i in range(len(nums)):
            if nums[i] == 1:
                if lastEncounter != -1:
                    if (i - lastEncounter)-1 < k:
                        return False
                lastEncounter = i
        return True