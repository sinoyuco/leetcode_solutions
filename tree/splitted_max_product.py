class Solution:
    def subtreesum(self, node):
        if not node:
            return 0
        l, r = self.subtreesum(node.left), self.subtreesum(node.right)
        return l+r+node.val

    def maxProduct(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.m = 0
        tot = self.subtreesum(root)

        def dfs(node):
            if not node:
                return 0
            l, r = dfs(node.left), dfs(node.right)
            s = l+r+node.val
            self.m = max(self.m, (tot-s)*s)
            return s
        dfs(root)
        return self.m % (10**9+7)
