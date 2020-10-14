class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # within the recursive calls, we are gonna pop the first element and make the recursive calls with the resulting
        # array. Therefore, our base involves the checking of if the length is 1, there is only 1 permutation, so we return that 2d array
        if len(nums) <= 1:
            return [nums]
        # up the order, for 2 elements, we know that we can only have 2 permutations (the elements switched)
        # In essence, the first popped element can be inserted either ahead or before the 
        f = nums.pop(0)
        rec_call = self.permute(nums)
        arr = []
        for i in rec_call:
            for j in range(len(i)+1):
                arr.append(i[:j]+[f]+i[j:])
        return arr
