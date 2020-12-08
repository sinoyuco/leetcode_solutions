import math
def getUmbrellas(requirement, sizes):
    # Write your code here
    sizes.sort()
    dp = [math.inf]*(requirement+1)
    dp[0] = 0
    for u in sizes:
        for j in range(u, requirement+1):
            dp[j] = min(dp[j], dp[j-u]+1)
    return dp[-1] if dp[-1] != math.inf else -1


print(getUmbrellas(7, [3,5]))
print(getUmbrellas(7, [1, 3, 5]))

