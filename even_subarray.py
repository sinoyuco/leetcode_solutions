def evenSubarray(numbers, k):
    # Write your code here
    count = 0
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            ct, a = 0, numbers[i:j+1]
            for num in a:
                if num % 2 != 0:
                    ct += 1
            if ct <= k:
                count += 1
    return count
