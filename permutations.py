class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        if len(nums) <= 1:
            print([nums])
            return [nums]

        f = nums.pop(0)
        rec_call = self.permute(nums)
        arr = []
        for i in rec_call:
            for j in range(len(i)+1):
                arr.append(i[:j]+[f]+i[j:])
        print(arr)
        return arr
