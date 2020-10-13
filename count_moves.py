def countMoves(numbers):
    # Write your code here
    # incrementing all but one in succession to make them all equal is EQUAL in effect to 
    # decrementing just one of them at each step until you reach the min.

    #Therefore, we just have to find the minimum value and go through the array once, adding to the count the difference
    # of each value and the minimum.
    m = min(numbers)
    ct = 0
    for i in numbers:
        ct += (i-m)
    return ct
