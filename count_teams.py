def countTeams(skills, minPlayers, minLevel, maxLevel):
    # Write your code here
    memo = {}

    def fact(n):
        if n in memo:
            return memo[n]
        elif n == 0:
            return 1
        else:
            x = fact(n-1) * n
            memo[n] = x
            return x

    ct = result = 0
    for i in range(len(skills)):
        if minLevel <= skills[i] <= maxLevel:
            ct += 1

    m = ct
    while ct >= minPlayers:
        result += fact(ct)/(fact(m) * fact(ct-m))
        ct -= 1
    return result
