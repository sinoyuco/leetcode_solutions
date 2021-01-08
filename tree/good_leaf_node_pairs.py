class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.s = 0

        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [[0, 0]]
            else:
                l, r = dfs(node.left), dfs(node.right)
                for i in l:
                    i[1] += 1
                for i in r:
                    i[1] += 1
                for i in r:
                    for j in l:
                        if i[1]+j[1] <= distance:
                            self.s += 1
                return l+r

        dfs(root)
        return self.s
