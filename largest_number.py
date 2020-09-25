def largestNumber(nums):
    def helper(num1, num2):
        str1 = num1+num2
        str2 = num2+num1
        return True if int(str1) < int(str2) else False

    def digitSort(lst):
        sorted = False
        while not sorted:
            sorted = True
            for i in range(len(lst)-1):
                if helper(str(lst[i]), str(lst[i+1])):
                    lst[i], lst[i+1] = lst[i+1], lst[i]
                    sorted = False
        return lst
        
    
    a = digitSort(nums)
    print(a)
    if sum(nums) == 0:
        return '0'
    return ''.join([str(x) for x in a])
