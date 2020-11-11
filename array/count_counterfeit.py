def countCounterfeit(serialNumber):
    # Write your code here
    valid = {10, 20, 50, 100, 200, 500, 1000}
    res = 0
    for i in range(len(serialNumber)):
        curr = serialNumber[i]
        if len(curr) < 10 or len(curr) > 12:
            continue
        if len(set(curr[0:3])) != 3:
            continue
        if curr[0].isnumeric() or curr[1].isnumeric() or curr[2].isnumeric():
            continue
        if curr[0].islower() or curr[1].islower() or curr[2].islower():
            continue

        if not curr[3:7].isnumeric():
            continue
        if int(curr[3:7]) < 1900 or int(curr[3:7]) > 2019:
            continue

        if not curr[7:-1].isnumeric():
            continue
        if int(curr[7:-1]) not in valid:
            continue

        if not curr[-1].isalpha():
            continue
        if curr[-1].islower():
            continue

        res += int(curr[7:-1])
    return res
