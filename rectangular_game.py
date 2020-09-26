def solve(steps):
    # maps = {}
    # max_val = 0
    # for i in steps:
    #     digits = i.split(' ')
    #     for j in range(1, int(digits[0])+1):
    #         for k in range(1, int(digits[1])+1):
    #             key = str(j)+str(k)
    #             if key in maps:
    #                 maps[key] += 1
    #             else:
    #                 maps[key] = 1

    #             if maps[key] > max_val: max_val = maps[key]
                

    # a = list(maps.values())
    # return a.count(max_val)
    x,y = [],[]
    for i in steps:
        b = i.split(' ')
        x_val,y_val = int(b[0]), int(b[1])
        x.append(x_val)
        y.append(y_val)
    return min(x) * min(y)



ex_steps = ['2 3', '4 7', '5 1']
b = print(solve(ex_steps))
