class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums)==1:
            return [nums]
        
        piv = nums.pop(0)
        
        rec_call = self.permuteUnique(nums)
        
        result = set()
        for c in rec_call:
            for i in range(len(c)+1):
                result.add(tuple(c[:i]+[piv]+c[i:]))
        return map(list, result)