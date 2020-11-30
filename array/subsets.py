class Solution:
    def helper(self, arr, idx):
        res = [[]]
        if idx == len(arr):
            return res
        for i in range(idx, len(arr)):
            c = arr[i]
            rec_call = self.helper(arr, i+1)
            for item in rec_call:
                res.append([c]+item)
        return res

    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.helper(nums, 0)
