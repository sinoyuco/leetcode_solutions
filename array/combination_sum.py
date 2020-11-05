def combinationSum(candidates, target):
    result = []

    def dfs(idx, target, right):
        if target < 0:
            return
        if target == 0:
            result.append(right)
            return
        for i in range(idx, len(candidates)):
            dfs(i, target-candidates[i], right+[candidates[i]])

            #dfs(0, 4, [1))
            #dfs(1, 3, [2])
    dfs(0, target, [])
    return result


print(combinationSum([2,3,6,7], 7))