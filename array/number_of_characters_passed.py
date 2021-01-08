def numberOfCharactersEscaped(expression):
    res = 0
    bol = False
    for i in range(len(expression)):
        c = expression[i]
        if c == '#':
            bol = not bol
        if c.isalpha() and i-1 > 0 and expression[i-1] == '!' and bol:
            res += 1
    return res
