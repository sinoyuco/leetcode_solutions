import collections
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:

        self.maxval = -math.inf
        self.res = -1

        def dfs(node, d):
            if not node:
                return
            if d > self.maxval:
                self.maxval = d
                self.res = node.val
            dfs(node.left, d+1)
            dfs(node.right, d+1)

        dfs(root, 0)
        return self.res
