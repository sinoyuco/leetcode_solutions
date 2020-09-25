def largestNumber(nums):
    def helper(num1, num2):
        i = 0
        while i < min(len(num1), len(num2)):
            if int(num2[i]) > int(num1[i]):
                return True
            elif int(num1[i]) > int(num2[i]):
                return False
            else:
                i+=1
    
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
    return ''.join([str(x) for x in a])