
class Helper(str):
    def __lt__(num1, num2):
        return num1+num2 > num2+num1
    
class Solution:

    def largestNumber(nums):

        # def digitSort(lst):
        #     sorted = False
        #     while not sorted:
        #         sorted = True
        #         for i in range(len(lst)-1):
        #             if helper(str(lst[i]), str(lst[i+1])):
        #                 lst[i], lst[i+1] = lst[i+1], lst[i]
        #                 sorted = False
        #     return lst
            
        
        # a = digitSort(nums)
        # print(a)
        # if sum(nums) == 0:
        #     return '0'
        # return ''.join([str(x) for x in a])
        nums = sorted(map(str, nums), key=Helper)
        return '0' if nums[0] == "0" else "".join(nums)

