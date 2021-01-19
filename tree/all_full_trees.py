class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N % 2 == 0:
            return []
        self.memo = {0: [], 1: [TreeNode(0)]}

        def dfs(num):
            if num not in self.memo:
                res = []
                for i in range(num):
                    j = num-(i+1)
                    for left in dfs(i):
                        for right in dfs(j):
                            c = TreeNode(0)
                            c.left, c.right = left, right
                            res.append(c)
                self.memo[num] = res
            return self.memo[num]

        return dfs(N)
