def combinationSum(candidates, target):
    result = []

    candidates = sorted(candidates)

    def dfs(idx, target, right):
        if target < 0:
            return
        if target == 0:
            result.append(right)
            return
        for i in range(idx, len(candidates)):
            dfs(i, target-candidates[i], right+[candidates[i]])

    dfs(0, target, [])
    return result


print(combinationSum([1,2], 5))