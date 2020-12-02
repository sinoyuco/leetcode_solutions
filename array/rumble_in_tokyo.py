def getMinimumBlows(height):
    if len(height) < 2:
        return 1
    # Write your code here
    s, e = 0, len(height)-1
    tot, ct = len(height), 0
    while tot > 0:
        ps, pe = s, e

        while ps+1 < len(height) and height[ps] <= height[ps+1]:
            ps += 1
        while pe-1 >= 0 and height[pe] <= height[pe-1]:
            pe -= 1

        if (ps-s) >= (e-pe):
            tot -= (ps-s)+1
        else:
            tot -= (e-pe)+1
        ct += 1
    return ct
