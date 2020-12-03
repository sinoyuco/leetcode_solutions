class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return []
        res = []
        nums.sort()
        for i in range(len(nums[:(n-2)])):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                break
                
            l,h = i+1,n-1
            while l < h:
                curr = nums[i] + nums[l] + nums[h]
                if curr < 0:
                    l+=1
                elif curr > 0:
                    h-=1
                else:
                    res.append([nums[i], nums[l], nums[h]])
                    while l < h and nums[l] == nums[l+1]:
                        l+=1
                    while l < h and nums[h] == nums[h-1]:
                        h-=1
                    l+=1
                    h-=1
                    
        return res